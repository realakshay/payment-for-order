from db import db
from datetime import datetime as dt
from models.item_in_order_model import ItemInOrderModel


class OrderModel(db.Model):
    __tablename__ = "neworders"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(30), nullable=False)
    total_bill = db.Column(db.Float(precision=2), nullable=False)
    purchase_date = db.Column(db.Date, default=dt.date(dt.now()))
    purchase_time = db.Column(db.Time, default=dt.time(dt.now()))

    items = db.relationship("ItemInOrderModel", back_populates="order")

    def insert_order(self):
        db.session.add(self)
        db.session.commit()

    def set_status(self, new_status:str):
        self.status = new_status
        self.insert_order()

    