import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
#from db import items
from schemas import ItemsSchema, ItemUpdateSchema


blp = Blueprint("items",__name__,description="Operations on Items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemsSchema)
    def get(self,item_id):
        try:
          return items[item_id]
        except KeyError:
          abort(404,message="Item not found")

    def delete(self,item_id):
       try:
          del items[item_id]
          return {"message": "Item Deleted"}
       except KeyError:
          abort(404,message="Item not found")
    @blp.arguments(ItemsSchema)
    @blp.response(200,ItemsSchema)       #order of decoraters matters so request will come before response
    def put(self,items_data,item_id):
      # items_data = request.get_json()  --> this is deleted as Schema is giving data and is now in parameters of Schema above  
    #**Validation Checks***
        #validation checks done by Schema (marshmallow)
        try:
          item = items[item_id]
          item |= items_data
          return item,201
        except KeyError:
           abort(404, message="Item not found")



@blp.route("/item")
class ItemList(MethodView):
   @blp.response(200,ItemsSchema(many=True))
   def get(self):
      return items.values() #{"items": list(items.values())}  --> since now the get returns list itself so no need to convert
   @blp.arguments(ItemsSchema)
   @blp.response(200,ItemsSchema)
   def post(self,items_data):    #item_data is the validated json which this method requested
      # items_data = request.get_json()  --> this is deleted as Schema is giving data

       #**Validation Checks***
       #CREATED USING MARSHMALLOW IN SCHEMAS FILE
       #2 Not to duplicate item which alreadu exist       
       for item in items.values():
          if(items_data["name"] == item["name"] and items_data["store_id"] == item["store_id"]):
             abort(400, message=f"Item already Exists")
       #3 If store does not exist
       #if items_data["store_id"] not in stores:
           # abort(404, message="Store not found")
                
       item_id = uuid.uuid4().hex
       item = {**items_data,"id":item_id}
       items[item_id]=item
       return item,201


