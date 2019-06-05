# 30th May 2019
# M3Engine (Workflow Engine) Handler Package
# Version 0.1
# Written by Mark, Mike, and Mac

from flask import Flask, jsonify, request
import os
import json

UserID = "Blah"

app = Flask(__name__)
#handlerapi_server = "HTTPS://127.0.0.1:5000"
handlerapi_server = "http://handlers.cfapps.io"

@app.route('/api/v1/handler/view',methods=['GET'])
def view():
    data = request.args
    
    userid = data ['userid']
    h_id = data ['h_id']
    
    apiuri = "/api/v1/read"
    parameters = {"h_id": h_id}

    view_response = requests.get(handlerapi_server + apiuri, params=parameters)
##    view_response = {'h_id': '1234', 'h_name': 'Joe Bloggs', 'h_servicedogid': '1234', 'h_trainerorg':'org'}
##    fake_view_response_code = 200

    if view_response.status_code == 200:
##    if fake_view_response_code == 200:
        response = view_response
        code = 200
    else:
        response = {'Result': 'Handler View: FAIL'}
        code = 400

    return jsonify(response), code

@app.route('/api/v1/handler/add',methods=['POST'])
def add():
    parameters = request.form
    apiuri = "/h_create"

    #print parameters
    
    # add_response = requests.post(handlerapi_server + apiuri, data=parameters)
    fake_add_response_code = 200
    
    #if add_response.status_code == 200:
    if fake_add_response_code == 200:
        response = {'Result': 'Handler Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Add - FAIL'}
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

    apiuri = "/h_delete"
    
    # delete_response = requests.delete(handlerapi_server + apiuri, data=parameters)
    fake_delete_response_code = 200

    #if delete_response.status_code == 200:
    if fake_delete_response_code == 200:
        response = {'Result': 'Handler Delete - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Delete - FAIL'}
        code = 400
        
    return jsonify (response), code 

@app.route('/api/v1/handler/update',methods=['PUT'])
def update():
    global userid
    global h_id

    data = request.form

    userid = data['userid']
    regid = data['h_id']

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
    #print parameters
    
    apiuri = "/h_update"
    
    # update_response = requests.put(handlerapi_server + apiuri, data=parameters)
    fake_update_response_code = 200
    
    #if update_response.status_code == 200:
    if fake_update_response_code == 200:
        response = {'Result': 'Handler Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Handler Update - FAIL'}
        code = 400
        
    return jsonify (response), code 

@app.route('/api/v1/handler/searchhandlerid',methods=['GET'])
def searchhandlerid():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/handler/searchbyname',methods=['GET'])
def searchbyname():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/handler/searchbyzip',methods=['GET'])
def searchbyzip():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')), threaded=True)
