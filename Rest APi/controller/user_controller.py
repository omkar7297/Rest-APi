from app import app
from flask import request,send_file
from model.user_model import user_model
from datetime import datetime

obj = user_model()

'''-------------------------------Show data Operation------------------------------------'''
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

'''-------------------------------Add Operation------------------------------------'''
@app.route("/user/addone",methods=["POST"])
def user_addone_controller():
    return obj.user_addone_model(request.form)

'''-------------------------------Update Operation------------------------------------'''
@app.route("/user/update",methods=["PUT"])
def user_update_controller():
    return obj.user_update_model(request.form)

'''-------------------------------Update by Patch method Operation------------------------------------'''
@app.route("/user/Update/<id>",methods=["PATCH"])
def user_Update_controller(id):
    return obj.user_Update_model(request.form,id)


'''-------------------------------Delete Operation------------------------------------'''
@app.route("/user/delete/<id>",methods=["DELETE"])
def user_delete_controller(id):
    return obj.user_delete_model(id)


'''-----------------------------Pagination Operation---------------------------------'''
@app.route("/user/getall/limit/<limit>/page/<page>",methods=["GET"])
def user_pagination_controller(limit,page):
    return obj.user_pagination_model(limit,page)



'''--------------------------File Uploading Operation-------------------------------'''
@app.route("/user/<uid>/upload/avtar",methods=["PUT"])
def user_upload_avtar(uid):
    file = request.files["avtar"]
    uniquename = str(datetime.now().timestamp()).replace(".","")
    filename = file.filename.split(".")
    extention = filename[len(filename)-1]
    finalname=(f"uploads/{uniquename}.{extention}")
    file.save(finalname)
    print(finalname)
    return obj.user_upload_model(finalname,uid)


@app.route("/uploads/<filename>")
def user_get_upload_file(filename):
    return send_file(f"uploads/{filename}")