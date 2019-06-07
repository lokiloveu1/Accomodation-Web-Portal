import os
import sqlite3
from sqlite3 import Error
import pandas as pd
from pandas.io import sql

from flask import Flask
from flask_restplus import Resource, Api, fields, inputs, reqparse

#from prediction.predict import important_factors, predict_target

#from flask_cors import CORS
from gevent.pywsgi import WSGIServer






app = Flask(__name__)
#CORS(app)
api = Api(app,default="api for Accommodation Web Portal",  
          title="Accommodation Web Portal", 
          description="api for Accommodation Web Portal")


#------------------------Operations about user-------------------------
user_model = api.model('user_account',{
    'email': fields.String
    'username': fields.String,
    'password': fields.String,
    })

@api.route('/api/user') #create user
class create_host(Resource):
    @api.response(201, 'user Created')
    @api.response(400,'Invalid input')
    @api.response(404,'Failed')
    def post(self):

        if request.content_type != JSON_MIME_TYPE:
            error = json.dumps({'error': 'Invalid Content Type'})
            return json_response(error, 400)

        input_payload = request.json
        
        if not input_payload.get('email'):
            return {"message":"Missing email"},400
        email = input_payload['email']
        email =str(email)
        #check if email already used
        
        if not input_payload.get('username'):
            return {"message":"Missing username"},400
        username = input_payload['username']
        username =str(username)
        #check if username already used; validation
        
        if not input_payload.get('password'):
            return {"message":"Missing password"},400
        password = input_payload['password']
        password =str(password)
        #check validation

        #assign an userid
        #if user table is empty,set userid as 0
        #otherwise get the latest user's id and plus 1

        return {"-"},200
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
@api.route('/api/user/login') # log in (Authenticate with the REST API)
class login(Resource):
   
    @api.response(200,'successfully loged in')
    @api.response(400,'Invalid input')
    @api.response(404,'Error') #User not exist / wrong password
    @api.doc(description="log in")
    @api.expect(user_model,validate=True)
    
    
    
if __name__ == '__main__':
 #   db_file = 'data.db'
 #   create_db(db_file)
    app.run(debug=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
