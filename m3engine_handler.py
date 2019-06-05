# 30th May 2019
# M3Engine (Workflow Engine) Handler Package
# Version 0.1
# Written by Mark, Mike, and Mac

from flask import Flask, jsonify, request
import os
import json
import requests

UserID = "Blah"

app = Flask(__name__)

if 'VCAP_SERVICES' in os.environ:
    hapi_server = "http://handlers.cfapps.io"
else: 
    hapi_server = "http://127.0.0.1:5000"

print(hapi_server)
hapi_base = hapi_server + "/api/v1"

## Test self
@app.route('/',methods=["GET"])
def root():
    print("I'm up and running")
    response = "vk-m3engine is up and running"
    return jsonify(response),200

## Test handlers microservices status
@app.route('/api/v1/handler/status',methods=["GET"])
def status():
    apiuri = "/status"

    handler_status = requests.get(hapi_base+apiuri)
    if handler_status:
        response = {'status': "Handlers API returns my ping"}
        code = 200
    else:
        response = {'statuscode': 400}
        code = 400
    return jsonify(response), code

## Call handler read API
@app.route('/api/v1/handler/view',methods=["GET"])
def view():
    apiuri = "/read"
    data = request.args
    
    userid = data['userid']
    h_id = data['h_id']
    payload = {'h_id': h_id}

    handler_response = requests.get(hapi_base+apiuri, params=payload)
    
    if handler_response:
        handler_content = json.loads(handler_response.content)
        response = handler_content
        code = 200
    else:
        response = {'Result': 'Handler View: FAIL'}
        code = 400
    
    return jsonify(response), code

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5050')), threaded=True)
