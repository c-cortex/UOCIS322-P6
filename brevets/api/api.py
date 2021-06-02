# List Times
from flask import Flask, request
from flask_restful import Resource, Api

import os
from pymongo import MongoClient

import json

from bson.json_util import loads, dumps


app = Flask(__name__)
api = Api(app)

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.tododb


class listAll(Resource):
    def get(self, dtype=""):
        times = list(db.tododb.find({},{"_id":0, "open": 1, "close": 1 }))
        if dtype == 'json':
            return loads(dumps(times))
        if dtype == 'csv':
            # cant get into csv form
            return loads(dumps(times))


class listOpenOnly(Resource):
    def get(self, dtype=""):
        top = request.args.get('top', type=int)
        app.logger.debug(top)
        times = db.tododb.find({},{"_id":0, "open": 1 })
        # cant get k to work
        # times = db.tododb.find({},{"_id":0, "open": 1 }).limit(top)
        # times = times[:top]
        if dtype == 'json':
            return loads(dumps(times))
        if dtype == 'csv':
            # cant get into csv form
            return loads(dumps(times))


class listCloseOnly(Resource):
    def get(self, dtype=""):
        top = request.args.get('top', type=int)
        app.logger.debug(top)
        times = list(db.tododb.find({},{"_id":0, "close": 1 }))
        # cant get k to work
        # times = db.tododb.find({},{"_id":0, "close": 1 }).limit(top)
        # times = times[:top]
        if dtype == 'json':
            return loads(dumps(times))
        if dtype == 'csv':
            # cant get into csv form
            return loads(dumps(times))


# Create routes
# Another way, without decorators
api.add_resource(listAll, '/listAll', '/listAll/<string:dtype>')
api.add_resource(listOpenOnly, '/listOpenOnly', '/listOpenOnly/<string:dtype>')
api.add_resource(listCloseOnly, '/listCloseOnly', '/listCloseOnly/<string:dtype>')


# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
