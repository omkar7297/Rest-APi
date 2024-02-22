import mysql.connector
import json
from flask import request
from flask import make_response


class user_model():
    '''----------------------------Construction---------------------------------'''
   
    def __init__(self):
        #First:-connection establishment
        try:
            self.con=mysql.connector.connect(host="localhost",username="root",password="",database="flask_turorial1")
            self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)   # it is a agent to have access to whole dataset and it is scheme to allow to do all operation

            print("connection done")
        except:
            print("There is some error in the database connection")


    '''-------------------------------Read Operation------------------------------------'''

    def user_getall_model(self):
        #Second:-second is sql query execution codes
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            res = make_response({"AllUser":result},200)
            res.headers['Access-Controle-Allow-Origin']='*'    # Response header
            return res   #here 200=ok status code
        else:
            return make_response({"msg":"No data found"},204)   #here 204=no data found status code
        
    
    '''-------------------------------Add Operation---------------------------------'''
    
    def user_addone_model(self,data):
        #self.cur.execute()
        #INSERT INTO customers (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com');
        qry=f"INSERT INTO users (name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')"
        self.cur.execute(qry)

        return make_response({"msg":"User Added Successfully"},201)  #here 200=Created
    

    '''--------------------Update Operation by put method-------------------------'''
   
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' WHERE id ={data['id']} ")
        if self.cur.rowcount>0:
           return make_response({"msg":"Data Updated"},201)
        else:
            return make_response({"msg":"Nothing to update"},202)
        


    '''--------------------Update Operation by Patch method-------------------------'''
   
    def user_Update_model(self,data,id):
        #row of query:-UPDATE users SET col=val, col=val where id={id}
        qry = "UPDATE users SET "
        for key in data:
            qry = qry + f"{key}='{data[key]}',"
        sliceqry=qry[:-1]
        complete_qry = sliceqry+f" WHERE id={id}"
        #print(complete_qry)
        self.cur.execute(complete_qry)
        if self.cur.rowcount>0:
            return make_response({"msg":"Changes Successfully complete"},201)
        else:
            return make_response({"msg":"Nothing To update"},202)
    


    '''-------------------------------Delete Operation---------------------------'''

    def user_delete_model(self,id):
        data = self.cur.execute(f"DELETE FROM users WHERE id ={id}")
        if self.cur.rowcount>0:
            return make_response({"msg":"delete done"},200)
        else:
            return make_response({"msg":"Nothing to delete"},202)


    '''-------------------------------Delete Operation---------------------------'''
    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start_point=int((page*limit)-limit)
        qry = f"SELECT * FROM users LIMIT {start_point},{limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        return result
    

    '''-------------------------------File upload Operation---------------------------'''
    def user_upload_model(self,finalname,uid):
        #print(finalname)
        self.cur.execute(f"UPDATE users SET avtar='{finalname}' WHERE id={uid}")
        if self.cur.rowcount>0:
           return make_response({"msg":"File Updated"},201)
        else:
            return make_response({"msg":"No File to upload"},202)