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

## Test for runtine location
if 'VCAP_SERVICES' in os.environ:
    handlerapi_server = "http://handlers.cfapps.io"
else: 
    handlerapi_server = "http://127.0.0.1:5000"
print("handlerapi_server: %s" % handlerapi_server)

## Test self
@app.route('/',methods=["GET"])
def root():
    print("I'm up and running")
    response = "m3engine is up and running"
    return jsonify(response),200

## Test handlers microservices status
@app.route('/api/v1/handler/status',methods=["GET"])
def status():
    apiuri = "/api/v1/status"

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
    apiuri = "/api/v1/read"
    data = request.args
    
    userid = data['userid']
    h_id = data['h_id']
    parameters = {'h_id': h_id}

    handler_response = requests.get(handlerapi_server + apiuri, params=parameters)
    
    if handler_response:
        handler_content = json.loads(handler_response.content)
        response = handler_content
        code = 200
    else:
        response = {'Result': 'Handler View: FAIL'}
        code = 400
    
    return jsonify(response), code

## Call handler create API
@app.route('/api/v1/handler/add',methods=['POST'])
def add():
    apiuri = "/api/v1/create"

    parameters = request.form
##    parameters.to_dict()

    add_response = requests.post(handlerapi_server + apiuri, json=parameters)
    
    if add_response:
        response = {'Result': 'Handler Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Add - FAIL'}
        code = 400
        
    return jsonify (response), code

## Call handler update API
@app.route('/api/v1/handler/update',methods=['PUT'])
def update():
    global userid
    global h_id

    data = request.form

    userid = data['userid']
    h_id = data['h_id']

    parameters = {'h_id':h_id}

    try:
        parameters['h_picture'] = data['h_picture']
    except:
        print "No change to Handler picture"
    try:
        parameters['h_servicedogid'] = data['h_servicedogid']
    except:
        print "No change to Handler service dog"
    try:
        parameters['h_trainerorg'] = data['h_trainerorg']
    except:
        print "No change to Handler organisation"
    print parameters
    
    apiuri = "/api/v1/update"
    
    update_response = requests.put(handlerapi_server + apiuri, json=parameters)
    
    if update_response.status_code:
        response = {'Result': 'Handler Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Update - FAIL'}
        code = 400
        
    return jsonify (response), code 

@app.route('/api/v1/handler/delete',methods=['DELETE'])
def delete():
    global userid
    global h_id
    
    data = request.form
    
    userid = data['userid']
    h_id = data['h_id']
    parameters = {'h_id':h_id}

    apiuri = "/api/v1/delete"
    
    delete_response = requests.delete(handlerapi_server + apiuri, params=parameters)
##    fake_delete_response_code = 200

    if delete_response:
##    if fake_delete_response_code == 200:
        response = {'Result': 'Handler Delete - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Delete - FAIL'}
        code = 400
        
    return jsonify (response), code 

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5050')), threaded=True)
