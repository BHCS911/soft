from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

from flask import Flask, render_template

import dbservice

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/')
def main():
    return render_template('manage-product.html')
    
    
    
@app.route('/getalldetails', methods=['GET'])
def get_all_details():
    response = dbservice.get_all_details(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertnewclient', methods=['POST'])
def insert_new_client():
    request_payload = json.loads(request.form['data'])
    client_id = dbservice.insert_new_client(connection, request_payload)
    response = jsonify({
        'client_id': client_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertnewstaff', methods=['POST'])
def insert_new_staff():
    request_payload = json.loads(request.form['data'])
    staff_id = dbservice.insert_new_staff(connection, request_payload)
    response = jsonify({
        'staff_id': staff_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





@app.route('/deleteclient', methods=['POST'])
def delete_client():
    client_id = dbservice.delete_client(connection, request.form['client_id'])
    response = jsonify({
        'client_id': client_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deletestaff', methods=['POST'])
def delete_staff():
    staff_id = dbservice.delete_staff(connection, request.form['client_id'])
    response = jsonify({
        'staff_id': staff_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(debug=True, port=5000)
    