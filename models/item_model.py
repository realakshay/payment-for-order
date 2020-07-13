from db import db
from typing import List


#simple item table which hold information about items i.e product (id, name, price)
class ItemModel(db.Model):
    __tablename__ = "newitems"         #sqlalchemy automatically catch this variable as table name 

    id = db.Column(db.Integer, primary_key=True)        #this id field is auto increment. no needd to give manually
    name = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float(precision=2), nullable=False)


    #This method will find id from items table and return the object of ItemModel
    @classmethod
    def find_by_id(cls, id:int) -> "ItemModel":
        return cls.query.filter_by(id=id).first()

    #Find the record by name
    @classmethod
    def find_by_name(cls, name:str) -> "ItemModel":
        return cls.query.filter_by(name=name).first()

    #This will return all items objects in List format [(id,name,price),(id,name,price)]
    @classmethod
    def find_all(cls) -> List:
        return cls.query.all()

    #This will insert object (name,price) in database
    def insert_item(self) -> None:
        db.session.add(self)
        db.session.commit()

    #This will delete object i.e. record from database
    def delete_item(self) -> None:
        db.session.delete(self)
        db.session.commit()