import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo    
#from library flask_pymongo, import Pymongo class/function

# from bson.objectid import ObjectId
# from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

from bson.json_util import dumps, loads
 #change this tasks object from mongodb

app = Flask(__name__)

#set configuration of the app
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
print(os.environ.get("MONGO_URI"))

mongo = PyMongo(app)

#home page 
@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)
    # tasks = mongo.db.tasks.find() #connect directly to mongo db name called tasks and get the tasks table (object)
    # json_string = dumps(tasks) #convert object into json string
    # return json_string

 
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)