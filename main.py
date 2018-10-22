from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

user_data = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

course_data = [
    {
        "name": "DevOps",
        "couse_id": "10/1000",
        "location": "Berlin"
    }
]


class User(Resource):
    '''Basic API Calls for User'''

    def get(self, name):
        for user in user_data:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404


class Course(Resource):
    def get(self, name):
        for course in course_data:
            if (name.lower() == (course["name"]).lower()):
                return course, 200
        return "Course not found", 404


if __name__ == '__main__':
    data = [{"name": "DevOps2", "couse_id": "10/1000","location": "Munich"}]
    course_data.append(data)


print(course_data)
api.add_resource(User, "/user/<string:name>")
api.add_resource(Course, "/course/<string:name>")
app.run(debug=True, port=7007)

