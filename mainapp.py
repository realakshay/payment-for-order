import os
from flask import Flask
from dotenv import load_dotenv
from db import db

load_dotenv('.env')

app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

@app.route('/')
def index():
    return "Hello World"

if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)