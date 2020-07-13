from db import db


#This is secondary table to manage many to many relationship
class ItemInOrderModel(db.Model):
    __tablename__ = "new_items_in_order"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("newitems.id"))
    order_id = db.Column(db.Integer, db.ForeignKey("neworders.id"))
    quantity = db.Column(db.Integer, nullable=False)

    item = db.relationship("ItemModel")
    order = db.relationship("OrderModel", back_populates="items")