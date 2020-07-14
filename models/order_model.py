import os
import stripe
from dotenv import load_dotenv
from db import db
from datetime import datetime as dt
from models.item_in_order_model import ItemInOrderModel

load_dotenv("/.env")

CURRENCY = 'inr'

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

    @property
    def make_description(self):
        items_count = [f"{item_data.quantity}x {item_data.item.name}" for item_data in self.items]	#suppose item is Bat and quantity is 3 then [Bat x 3]
        return ",".join(items_count)

    def create_token(self):
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')        #Test stripe secret key
        token = stripe.Token.create(
		
            #Dummy card details for testing purpose
	        card={
		        "number": "4242424242424242",
                	"exp_month": 7,
                	"exp_year": 2021,
                	"cvc": "314",
  	        },
        )
        return token

    def make_payment_stripe(self, token):
        stripe.api_key = os.getenv('STRIPE_SECRET_KEY')     #Test stripe secret key
        return stripe.Charge.create(
            amount=int(self.total_bill)*100,			#here 500 means rs 5.00
            currency=CURRENCY,
            description=self.make_description,
            source=token
        )
