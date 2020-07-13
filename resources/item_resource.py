from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from models.item_model import ItemModel
from schemas.item_schema import ItemSchema


item_schema = ItemSchema()                  #Only one object will handle
items_schema = ItemSchema(many=True)        #For operate more than objects or rows


class Item(Resource):

    @classmethod
    def post(cls):
        json_data = request.get_json()
        try:                                        #Check input data whether valid or not
            item_data = item_schema.load(json_data)     #It will export json to dict 
        except ValidationError as err:              #invalid data exception handle
            return err.messages, 400
        
        item = ItemModel.find_by_name(item_data['name'])
        if item:
            return {"Message" : "The item with name {} is already exists in table".format(item_data['name'])}, 400
        
        item = ItemModel(**item_data)               #Created ItemModel object
        item.insert_item()
        return {"Message" : "Item inserted successfully"}, 201


class ItemList(Resource):

    @classmethod
    def get(cls):
        return {"Items" : items_schema.dump(ItemModel.find_all())}, 200