
from email import message
import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.store import StoreModel
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
#from db import stores
from schemas import StoreSchema
from db import db

blp = Blueprint("stores",__name__,description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Stores(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store
        """ try:
          return stores[store_id]
        except KeyError:
           abort(404,message="Store not found") """
    def delete(self, store_id):
       store =  StoreModel.query.get_or_404(store_id)
       db.session.delete(store)
       db.session.commit()
       return {"message":"Store Deleted"}
       """  try:
           del stores[store_id]
           return {"message": "Store Deleted"}
        except KeyError:
            abort(404,message="Store not found") """

    @blp.route("/store")
    class StoreList(MethodView):
       @blp.response(200,StoreSchema(many=True))
       def get(self):
          return StoreModel.query.all() #{"stores": list(stores.values())}
       @blp.arguments(StoreSchema)
       @blp.response(200,StoreSchema)
       def post(self,store_data):
          store = StoreModel(**store_data)
          try:
             db.session.add(store)
             db.session.commit()
          except IntegrityError:
             abort(400,message="A with that name already exisits")
          except SQLAlchemyError:
             abort(500,message="An error occured while creating store")
          return store
         # store_data = request.get_json() --> this is now coming validated from Schema marhsmallow
          """ if "name" not in store_data:
             abort(400, message="Bad Request ! Ensur name is present") """ # --> this validation is already done in Schema
          """ for store in stores.values():
             if store["name"] == store_data["name"]:
                abort(400, message = "Store already Exists")   #all tnis will be done by models and schema no need to validate here
        
          store_id = uuid.uuid4().hex
          store = {**store_data,"id":store_id}
          stores[store_id] = store """
          