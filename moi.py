# moi.py
# Copyright 2017 Tero Karvinen http://TeroKarvinen.com

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///training'
app.config['SECRET_KEY'] = 'k377AglooNex+932.asdjReajeIxane436'

users = [
{
         "name": "Sven",
         "age": 42,
         "occupation": "Network Engineer"
     }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if (name == user["name"]):
                return user, 200
        return "User not found", 404


def sql(rawSql, sqlVars={}):
    "Execute raw sql, optionally with prepared query"
    assert type(rawSql) == str
    assert type(sqlVars) == dict
    res = db.session.execute(rawSql, sqlVars)
    db.session.commit()
    return res

@app.before_first_request
def initDBforFlask():
 sql("CREATE TABLE IF NOT EXISTS student (id SERIAL PRIMARY KEY, fstname VARCHAR(255), lstname VARCHAR(255) , qnummer VARCHAR(7) unique, department VARCHAR(15));")
@app.route("/")
def hello():
 return "See you at TeroKarvinen.com! <a href='/students'>List Students</a>\n"

@app.route("/students")
def animals():
    stamm = 'q237012'
    students=sql("SELECT * FROM student where qnummer = 'q237012';")
    return render_template("student.html", animals=students)

@app.route("/courses")
def test():
 trainings = sql("SELECT * FROM courses order by training_id;")
 return render_template("courses.html", trainings=trainings)

api.add_resource(User, "/user/<string:name>")

if __name__ == "__main__":

 app.run(debug=True, port=7007)