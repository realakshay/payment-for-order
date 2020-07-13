import os
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from resources.item_resource import Item, ItemList
from resources.order_resource import Order

load_dotenv('.env')

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')


@app.before_first_request
def create_table():
    db.drop_all()
    db.create_all()

@app.route('/')
def index():
    return "Hello World"

api.add_resource(Item, '/items')
api.add_resource(ItemList, '/allitems')
api.add_resource(Order,'/order')

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)