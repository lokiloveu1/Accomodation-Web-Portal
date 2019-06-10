from app import app, db
from app.models import User
from flask_restplus import Resource, Api, fields, inputs, reqparse

api = Api(app,default="api for Accommodation Web Portal",  
          title="Accommodation Web Portal", 
          description="api for Accommodation Web Portal")

@api.route('/api/user') #create user
class RegisterUser(Resource):
    @api.response(201, 'User created')
    @api.response(400,'Invalid input')
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username', required=True, help='Username cannot be blank.')
        parser.add_argument('email', required=True, help='Email cannot be blank.')
        parser.add_argument('password', required=True, help='Password cannot be blank.')
        parser.add_argument('is_host')
        args = parser.parse_args()

        new_user = User(
            username=args.username,
            email=args.email,
        )

        # hashes input password, and sets password_hash field
        new_user.set_password(args.password)
        db.session.add(new_user)

        # handle this error. duplicate email/username, etc.
        db.session.commit()

        return {'msg': 'user successfully created'}, 201
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
# @api.route('/api/user/login') # log in (Authenticate with the REST API)
# class login(Resource):
   
#     @api.response(200,'successfully loged in')
#     @api.response(400,'Invalid input')
#     @api.response(404,'Error') #User not exist / wrong password
#     @api.doc(description="log in")
#     @api.expect(user_model,validate=True)
