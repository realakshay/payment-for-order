from marshmallow import Schema, fields
from models.order_model import OrderModel
from schemas.item_schema import ItemSchema

class OrderSchema(Schema):
    class Meta:
        model = OrderModel
    id = fields.Int(dump_only=True)
    status = fields.Str()
    total_bill = fields.Float()
    purchase_date = fields.Date(dump_only=True)
    purchase_time = fields.Time(dump_only=True)

    items = fields.Nested(ItemSchema, many=True)        #It will held items related to that order