from flask import Blueprint, request
from .db import connect_db

client = connect_db()

#db --> database name
#crud_table --> table name
OBJ = client.db.crud_table

crud_api = Blueprint('crud_api', __name__, url_prefix='/crud')

@crud_api.post('/create')
def create_api():
    data = request.get_json()
    index_id ={"_id" : OBJ.count_documents({}) + 1}
    index_id.update(data)
    OBJ.insert(index_id)
    return {"status":"success", "result":list(OBJ.find())}

@crud_api.put('/update')
def update_api():
    data = request.get_json()
    OBJ.update({"_id":data['_id']},data)
    return {"status": "success", "result":list(OBJ.find({"_id":data["_id"]}))}
@crud_api.get('/get/<string:id>')
def get_api(id):
    return {"status": "success", "result":list(OBJ.find({"_id":int(id)}))}
@crud_api.get("/all")
def all_api():
    return {"status": "success", "result":list(OBJ.find({}))}
@crud_api.delete("/delete/<string:id>")
def delete_api(id):
    return {"status": "success", "result":list(OBJ.remove({"_id":int(id)}))}
