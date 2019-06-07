from app import app
from flask_restplus import Resource, Api, fields, inputs, reqparse

api = Api(app,default="api for Accommodation Web Portal",  
          title="Accommodation Web Portal", 
          description="api for Accommodation Web Portal")

@api.route('/api/user') #create user
class User(Resource):
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

        return {'msg': 'user successfully created'}, 201
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# @api.route('/api/user/login') # log in (Authenticate with the REST API)
# class login(Resource):
   
#     @api.response(200,'successfully loged in')
#     @api.response(400,'Invalid input')
#     @api.response(404,'Error') #User not exist / wrong password
#     @api.doc(description="log in")
#     @api.expect(user_model,validate=True)
