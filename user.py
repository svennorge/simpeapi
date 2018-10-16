from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

class user(Resource):

    dataJson = 'user.json'
    users = []

    def __init__(self):
        '''create the data.json file if it dows not exists'''

        try:
            with open(self.dataJson,  'r') as infile:
                self.users = json.load(infile)
        except FileNotFoundError:
            with open(self.dataJson, 'w') as outfile:
                json.dump(self.users, outfile)


    def get(self, name):
        with open(self.dataJson) as infile:
            self.users = json.load(infile)
        for user in self.users:
            if (name == user["name"]):
                return user, 200
            else:
                with open(self.dataJson, 'w') as outfile:
                    json.dump(self.users, outfile)
                return self.users, 200;
        return "User not found", 404

class course(Resource):

    dataJson = 'course.json'
    course = []

    def __init__(self):
        '''create the data.json file if it dows not exists'''

        try:
            with open(self.dataJson,  'r') as infile:
                self.course = json.load(infile)
        except FileNotFoundError:
            with open(self.dataJson, 'w') as outfile:
                json.dump(self.course, outfile)

    def get(self, name):
        with open(self.dataJson) as infile:
            self.course = json.load(infile)
        for user in self.course:
            if (name == user["name"]):
                return user, 200
            else:
                with open(self.dataJson, 'w') as outfile:
                    json.dump(self.users, outfile)
                return self.course, 200;
        return "course not found", 404


api.add_resource(user, "/user/<string:name>")
api.add_resource(course, "/course/<string:name>")

app.run(debug=True, port=7070)
