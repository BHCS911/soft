from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

from flask import Flask, render_template

import python

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/')
def main():
    return render_template('web\manage-product.html')
    
    
    
@app.route('/getalldetails', methods=['GET'])
def get_all_details():
    response = python.get_all_details(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertnewclient', methods=['POST'])
def insert_new_client():
    request_payload = json.loads(request.form['data'])
    product_id = python.insert_new_client(connection, request_payload)
    response = jsonify({
        'client_id': client_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertnewstaff', methods=['POST'])
def insert_new_staff():
    request_payload = json.loads(request.form['data'])
    product_id = python.insert_new_staff(connection, request_payload)
    response = jsonify({
        'staff_id': staff_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response





@app.route('/deleteclient', methods=['POST'])
def delete_client():
    return_id = python.delete_client(connection, request.form['client_id'])
    response = jsonify({
        'client_id': client_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deletestaff', methods=['POST'])
def delete_staff():
    return_id = python.delete_staff(connection, request.form['client_id'])
    response = jsonify({
        'staff_id': staff_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)