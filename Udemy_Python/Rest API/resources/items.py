import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("items",__name__,description="Operations on Items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id) #now its feature of flask alchemy that we can query db through model
                                                   #and the item_id will pull data by primary key and if id not there throw 404 error
        return item
        """ try:
          return items[item_id] --> this is commented as now we are getting data from database instead of item dict
        except KeyError:
          abort(404,message="Item not found") """

    def delete(self,item_id):
      item = ItemModel.query.get_or_404(item_id)
      db.session.delete(item)
      db.session.commit()
      return {"message":"Item Deleted"}
      
    
      """  try:
          del items[item_id]
          return {"message": "Item Deleted"}
       except KeyError:
          abort(404,message="Item not found") """
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)       #order of decoraters matters so request will come before response
    def put(self,items_data,item_id):
       item = ItemModel.query.get(item_id)
       if item:
         item.price = items_data["price"]
         item.name = items_data["name"]
       else:
          item = ItemModel(id=item_id,**items_data)
       db.session.add(item)
       db.session.commit()
       
      # items_data = request.get_json()  --> this is deleted as Schema is giving data and is now in parameters of Schema above  
    #**Validation Checks***
        #validation checks done by Schema (marshmallow)
       """  try:
          item = items[item_id]
          item |= items_data
          return item,201
        except KeyError:
           abort(404, message="Item not found") """



@blp.route("/item")
class ItemList(MethodView):
   @blp.response(200,ItemSchema(many=True))
   def get(self):
      return ItemModel.query.all() #{"items": list(items.values())}  --> since now the get returns list itself so no need to convert
   @blp.arguments(ItemSchema)
   @blp.response(200,ItemSchema)
   def post(self,items_data):     #item_data is the validated json which this method requested
       item = ItemModel(**items_data)
       try:
          db.session.add(item)
          db.session.commit()
       except SQLAlchemyError:
          abort(500, message="An error occured while inserting the Item")
       return item,201      
      # items_data = request.get_json()  --> this is deleted as Schema is giving data

       #**Validation Checks***
       #CREATED USING MARSHMALLOW IN SCHEMAS FILE
       #2 Not to duplicate item which alreadu exist       
       """ for item in items.values():
          if(items_data["name"] == item["name"] and items_data["store_id"] == item["store_id"]):
             abort(400, message=f"Item already Exists") """ #--> this check is now done in models
       #3 If store does not exist
       #if items_data["store_id"] not in stores:
           # abort(404, message="Store not found")
                
       """ item_id = uuid.uuid4().hex
       item = {**items_data,"id":item_id}
       items[item_id]=item """
       


