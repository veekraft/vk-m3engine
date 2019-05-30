# 30th May 2019
# M3Engine (Workflow Engine) Dog Package
# Version 0.1
# Written by Mark, Mike, and Mac

from flask import Flask, jsonify, request
import os
import json

UserID = "Blah"

app = Flask(__name__)
dogapi_server = "127.0.0.1"

@app.route('/api/v1/dog/view',methods=['GET'])
def view():
    # Request should be of form "userID, sd_regid", store in local variables.
    data = request.args
    
    userid = data ['userid']
    regid = data ['sd_regid']
    
    apiuri = "/sd_read"
    parameters = {"sd_regid": regid}
    
    #view_response = requests.get("https://" + dogapi_server + apiuri, params=parameters)

    # Fake Return Dog Data
    view_response = {'sd_regid': '1234', 'sd_name': 'fido', 'sd_regstatus': 'Registered', 'sd_teamstatus':'Approved'}
    # Fake Response
    fake_view_response_code = 200

    #if view_response.status_code == 200:
    if fake_view_response_code == 200:
        response = view_response
        code = 200
    else:
        response = {'Result: Error viewing Dog Entry'}
        code = 400

    return jsonify(response), code

@app.route('/api/v1/dog/add',methods=['POST'])
def add():
    #Request should be of the form:
    # { sd_name: Dog Name
    #   sd_regstatus : Registration Status
    #   sd_expiredate : Expiry Date
    #   sd_teamstatus : Team Status (Approved/Expired/Flagged)
    #   sd_handlerid: Handler ID
    #   sd_vaccstatus: Vaccination Status
    #   sd_vaccepiredate: Vaccination Expiry Date
    #   sd_pedigree: Breed
    #   sd_trainername: Trainer Name
    #   sd_trainerorg: Trainer Organisation
    # } 
    parameters = request.form
    
    apiuri = "/sd_create"

    #print parameters
    
    # add_response = requests.post("https://" + dogapi_server + apiuri, params=parameters)
    # Fake Response
    fake_add_response_code = 200
    
    #if add_response.status_code == 200:
    if fake_add_response_code == 200:
        response = {'Result': 'Dog Add - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Add - FAIL'}
        code = 400
        
    return jsonify (response), code 
    
@app.route('/api/v1/dog/delete',methods=['DELETE'])
def delete():
    #userid, regid needed to set inactive status
    data = request.form
    global userid
    global regid

    userid = data['userid']
    regid = data['sd_regid']
    parameters = {'sd_regid':regid, 'sd_regstatus': 'False', 'sd_teamstatus': 'Expired'}

    apiuri = "/sd_delete"
    # delete_response = requests.post("https://" + dogapi_server + apiuri, params=parameters)
    fake_delete_response_code = 200

    #if delete_response.status_code == 200:
    if fake_delete_response_code == 200:
        response = {'Result': 'Dog Retire - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Retire - FAIL'}
        code = 400
        
    return jsonify (response), code 

@app.route('/api/v1/dog/update',methods=['PUT'])
def update():
    #Request items that can be updated:
    #   sd_regstatus : Registration Status
    #   sd_expiredate : Expiry Date
    #   sd_teamstatus : Team Status (Approved/Expired/Flagged)
    #   sd_handlerid: Handler ID
    #   sd_vaccstatus: Vaccination Status
    #   sd_vaccepiredate: Vaccination Expiry Date
    #   sd_trainername: Trainer Name
    #   sd_trainerorg: Trainer Organisation
    data = request.form

    global userid
    global regid

    userid = data['userid']
    regid = data['sd_regid']

    parameters = {'sd_regid':regid}

    # Allow update but also allow variable set to fail.
    try:
        parameters['sd_regstatus'] = data['sd_regstatus']
    except:
        print "No change to registration data"
    try:
        parameters['sd_expiredate'] = data['sd_expiredate']
    except:
        print "No change to expiry date"
    try:
        parameters['sd_teamstatus'] = data['sd_teamstatus']
    except:
        print "No change to Team Status"
    try:
        parameters['sd_handlerid'] = data['sd_handlerid']
    except:
        print "No change to Handler ID"
    try:
        parameters['sd_vaccstatus'] = data['sd_vaccstatus']
    except:
        print "No Change to Vaccination Status"
    try:
        parameters['sd_vaccexpiredate'] = data['sd_vaccexpiredate']
    except:
        print "No change to Vaccination Expiry"
    try:
        parameters['sd_trainername'] = data['sd_trainername']
    except:
        print "No change to Trainer Organisation"
    try:
        parameters['sd_trainerorg'] = data['sd_trainerorg']
    except:
        print "No change to Trainer Organisation"

    #print parameters
    
    apiuri = "/sd_update"
    
    # update_response = requests.post("https://" + dogapi_server + apiuri, params=parameters)
    # Fake Response
    fake_update_response_code = 200
    
    #if update_response.status_code == 200:
    if fake_update_response_code == 200:
        response = {'Result': 'Dog Update - SUCCESS'}
        code = 200
    else:
        response = {'Result': 'Dog Update - FAIL'}
        code = 400
        
    return jsonify (response), code 

@app.route('/api/v1/dog/searchdogid',methods=['GET'])
def searchdogid():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchbyname',methods=['GET'])
def searchbyname():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchbyzip',methods=['GET'])
def searchbyzip():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchavailablebyzip',methods=['GET'])
def searchavailablebyzip():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

@app.route('/api/v1/dog/searchvaccination',methods=['GET'])
def searchvaccination():
    response = {'Result': 'Not Implemented'}
    code = 200
    return jsonify (response), code

#Ucomment for unit testing
if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5010')))
