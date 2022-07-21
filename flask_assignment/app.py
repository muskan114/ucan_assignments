from flask import Flask
from flask import request

app = Flask(__name__)

STUDENTS = {
    "navdeep" : {
        "first_name": "Navdeep",
        "last_name": "Sapra" ,
        "email" : "navdeep.sapra@ucan.com",
        "age" : "21",
        "gender": "Male",
        "college_name" : "GNDEC"
    },
    "muskan" :{
        "first_name": "Muskan",
        "last_name" : "Dhillon",
        "email":"muskan.dhillon@ucan.com",
        "age" : "21",
        "gender" : "Female",
        "collge_name" : "GNDEC"
    }
}

@app.route("/info/personal", methods=['POST'])
def create_info():
    body = request.json
    print("REQUEST BODY:", body)
    print(type(body))
    print("First name", body['first_name'])
    return body

@app.route("/info/personal/<username>", methods=['GET'])
def get_info(username):
    return STUDENTS[username]
               

if __name__ =='__main__':
    app.run(debug = True)
