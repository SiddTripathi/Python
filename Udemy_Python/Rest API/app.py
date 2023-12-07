from email import message
from flask import Flask, request
from flask_smorest import abort

import uuid
app = Flask(__name__)
from db import items,stores

#Temporary Data base



@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores": list(stores.values())}

@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404,message="Store not found")

@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Bad Request ! Ensur name is present")
    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message = "Store already Exists")
        
    store_id = uuid.uuid4().hex
    store = {**store_data,"id":store_id}
    stores[store_id] = store
    return store,201

@app.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store Deleted"}
    except KeyError:
        abort(404,message="Store not found")






@app.get("/item")
def get_all_items():
   
    return {"items": list(items.values())}

@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404,message="Item not found")

@app.post("/item")
def create_item():
    items_data = request.get_json()
    #**Validation Checks***

    #1 To ensure price name and store id is present while creating item
    if("price" not in items_data or "store_id" not in items_data  or "name" not in items_data):
        abort(400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")
    #2 Not to duplicate item which alreadu exist       
    for item in items.values():
        if(items_data["name"] == item["name"] and items_data["store_id"] == item["store_id"]):
            abort(400, message=f"Item already Exists")
    #3 If store does not exist
    if items_data["store_id"] not in stores:
        abort(404, message="Store not found")
    
    
    item_id = uuid.uuid4().hex
    item = {**items_data,"id":item_id}
    items[item_id]=item
    return item,201



@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item Deleted"}
    except KeyError:
        abort(404,message="Item not found")


@app.put("/item/<string:item_id>")
def update_item(item_id):
    items_data = request.get_json()
    #**Validation Checks***
    if("price" not in items_data or "name" not in items_data):
        abort(400,
            message="Bad request. Ensure 'price', 'store_id', and 'name' are included in the JSON payload.")
    try:
        item = items[item_id]
        item |= items_data
        return item,201
    except KeyError:
        abort(404, message="Item not found")

    
    
    
    #for item in items.values():
     #   if item_id != item["id"]:
      #      abort(404, message="item not found")
       # else:
        #     item = {**items_data,"id":item_id,"store_id": item["store_id"]}
         #    items[item_id]=item
          #   return item,201
   