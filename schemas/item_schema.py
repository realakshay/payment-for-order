from marshmallow import Schema, fields
from models.item_model import ItemModel

class ItemSchema(Schema):
    class Meta:
        model = ItemModel
    id = fields.Int(dump_only=True)     #auto increment by default. dump_only means we only fetch from db
    name = fields.Str(required=True)
    price = fields.Float(required=True)