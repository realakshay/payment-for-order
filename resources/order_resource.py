from collections import Counter
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from schemas.order_schema import OrderSchema
from models.item_model import ItemModel
from models.order_model import OrderModel
from models.item_in_order_model import ItemInOrderModel

order_schema = OrderSchema()


class Order(Resource):

    @classmethod
    def post(cls):
        json_data = request.get_json()          # input {'item_ids':[1,2,3,4,1,1,1]}
        items = []

        ''' Counter will count the number with occurences
            {'item_ids':[1,2,3,4,1,1,1]}
            It will count the id with quanity i.e [(1,4),(2,1),(3,1),(4,1)]
        '''

        items_id_quantity = Counter(json_data['item_ids'])  
        total_amount = 0

        for id, count in items_id_quantity.most_common():    
            item = ItemModel.find_by_id(id)
            total_amount = total_amount + item.price * count        #add new item price to find total bill
            if not item:
                return {"Message": "Item with id {} is not available".format(id)}, 400
            items.append(ItemInOrderModel(item_id=id, quantity=count))

        order = OrderModel(items=items, status="pending", total_bill=total_amount)      #initially status is pending
        order.insert_order()
        order.set_status("failed")          #before payment done status is failed if so
        token = order.create_token()        #after getting card details we will make token
        order.make_payment_stripe(token)    #make payment
        order.set_status("completed")       #after payment done status will be 
        return {"order" : order_schema.dump(order)}, 200