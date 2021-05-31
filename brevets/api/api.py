# List Times
from flask import Flask, request
from flask_restful import Resource, Api

import os
from pymongo import MongoClient

import json

from bson import json_util

app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client["database"]
collection = db["brevtimes"]


class listAll(Resource):
    def get(self, dtype=""):
        top = request.args.get("k", type=int)
        times = list(collection.find({},{"_id":0, "open": 1, "close": 1 }))
        if dtype == 'json':
            return json.loads(json_util.dumps(times))
        if dtype == 'csv':
            for x in collection.find({},{"_id":0, "open": 1, "close": 1 }):
                return json.loads(x)


class listOpenOnly(Resource):
    def get(self, dtype=""):
        top = request.args.get("k", type=int)
        times = list(collection.find({},{"_id":0, "open": 1 }))
        if dtype == 'json':
            return json.loads(json_util.dumps(times))
        if dtype == 'csv':
            for x in collection.find({},{"_id":0, "open": 1 }):
                return json.loads(x)


class listCloseOnly(Resource):
    def get(self, dtype=""):
        top = request.args.get("k", type=int)
        times = list(collection.find({},{"_id":0, "close": 1 }))
        if dtype == 'json':
            return json.loads(json_util.dumps(times))
        if dtype == 'csv':
            for x in collection.find({},{"_id":0, "close": 1 }):
                return json.loads(x)


# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll', '/listAll/<string:dtype>')
api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/<string:dtype>')
api.add_resource(listCloseOnly, '/listCloseOnly', '/listCloseOnly/<string:dtype>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
