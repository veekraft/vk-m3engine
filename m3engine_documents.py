from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

docapi = "https://127.0.0.1" #This will change


@app.route('/api/v1/document/add',methods=['POST'])
def add():

    # Receive data from UI
    mydata = request.form # Put POST request data in a dictionary
    print mydata
    #Data Transformation - TBA based on what UI sends us

    # Send data to document
    uri = "/api/v1/document/add" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.post(uri, data=mydata)
    #obj = json.loads(response.content)

    code = 500

    try:
        print "sending POST containing: " + str(mydata) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 401
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(mydata), code


@app.route('/api/v1/document/searchbyid',methods=['GET'])
def searchbyid():

    print 'BZLAJ'
    # Receive data from UI
    mydata = request.args # Put GET request data in a dictionary
    print mydata
    #Data Transformation - TBA based on what UI sends us

    handlerid = mydata['handlerid']

    # Send data to document
    uri = "/api/v1/document/searchbyid" #This might change depending on what the document guys do
    url = docapi + uri

    #response = requests.get(uri, params=mydata)
    #obj = json.loads(response.content)

    # Fake Return Document Data
    view_response = {'documentid': '1234', 'handlerid': handlerid, 'dogid': '1011', 'imageurl': 'https://ecs/image.png'}

    # Fake Response
    try:
        print "sending GET containing: " + str(view_response) + " to:" + url
    except ValueError:
        response = "FAIL"
        code = 400
        print response
    else:
        response = "SUCCESS"
        code = 200

    #return jsonify(response), code # use this once we have a target that will return
    return jsonify(view_response), code


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
