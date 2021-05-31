from flask import Flask, render_template, request, jsonify
import requests
import flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    app.logger.debug("Index")
    return flask.render_template('index.html')


@app.route('/listAll')
def listAll():
    app.logger.debug("List of All")
    format = request.args.get("format", type=str)
    k = request.args.get("k", type=int)
    app.logger.debug(k)
    if format == "json":
        rslt = requests.get(f"http://restapi:5000/listAll/json?top={k}")
    if format == "csv":
        rslt = requests.get(f"http://restapi:5000/listAll/csv?top={k}")
    return rslt.text


@app.route('/listOpenOnly')
def listOpenOnly():
    app.logger.debug("List of Open Only")
    format = request.args.get("format", type=str)
    k = request.args.get("k", type=int)
    if format == "csv":
        rslt = requests.get(f"http://restapi:5000/listOpenOnly/csv?top={k}")
    if format == "json":
        rslt = requests.get(f"http://restapi:5000/listOpenOnly/json?top={k}")
    return rslt.text



@app.route('/listCloseOnly')
def listCloseOnly():
    app.logger.debug("List of Close Only")
    format = request.args.get("format", type=str)
    k = request.args.get("k", type=int)
    if format == "csv":
        rslt = requests.get(f"http://restapi:5000/listCloseOnly/csv?top={k}")
    if format == "json":
        rslt = requests.get(f"http://restapi:5000/listCloseOnly/json?top={k}")
    return rslt.text



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
