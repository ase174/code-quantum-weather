from flask import Flask, make_response, jsonify
import json
import graph 
#from flask_cors import CORS
#import ./createData
import sys

app = Flask(__name__)

@app.route("/")
def sendData():
    resp = make_response(
            jsonify(
                {"hello world":'abc'}
                ),
                200,
            )
    resp.headers["Content-Type"] = "application/json"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp
@app.route("/getDailyImg")
def sendImg():
    imgName = graph.makeGraph()
    resp = make_response(
            jsonify(
                {"imgName": imgName}
                ),
                200,
            )
    print(imgName, file=sys.stderr)
    resp.headers["Content-Type"] = "application/json"
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp
