from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class user(Resource):
    jsonfile = 'data.json'
    users = []

    def __init__(self):
        '''create the data.json file if it dows not exists'''

        try:
            with open(self.jsonfile,  'r') as infile:
                self.users = json.load(infile)
        except FileNotFoundError:
            with open(self.jsonfile, 'w') as outfile:
                json.dump(self.users, outfile)


    def get(self, name):
        with open('data.json') as infile:
            users = json.load(infile)
        for user in users:
            if (name == user["name"]):
                return user, 200
            else:
                with open('data.json', 'w') as outfile:
                    json.dump(users, outfile)
                return users, 200;
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        parser.add_argument("location")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"],
            "location": args["location"]
        }
        users.append(user)
        with open('data.json', 'w') as outfile:
            json.dump(users, outfile)
        return user, 201

    def put(self, name):
        with open('data.json') as infile:
            users = json.load(infile)
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        parser.add_argument("location")
        args = parser.parse_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                user["location"] = args["location"]
                return user, 200

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"],
            "location": args["location"]
        }
        users.append(user)
        with open('data.json', 'w') as outfile:
            json.dump(users, outfile)
        return user, 201

    def delete(self, name):
        # global users
        users = [user for user in users if user["name"] != name]


        return "{} is deleted.".format(name), 200


api.add_resource(user, "/user/<string:name>")

app.run(debug=True)
