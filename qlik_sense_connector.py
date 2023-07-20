# qlik_sense_connector.py

import requests
import json

def connect():
    # Replace 'your_qlik_sense_api_url' with the actual Qlik Sense API URL
    qlik_sense_conn = requests.get('your_qlik_sense_api_url')

    if qlik_sense_conn.status_code == 200:
        print("Connected to Qlik Sense")
        return qlik_sense_conn
    else:
        print("Failed to connect to Qlik Sense")
        return None

def load_data(connection, data):
    # Replace 'your_qlik_sense_load_url' with the actual Qlik Sense load URL
    load_data = requests.post('your_qlik_sense_load_url', json=data, headers=connection.headers)
    if load_data.status_code == 200:
        print("Data loaded into Qlik Sense")
    else:
        print("Failed to load data into Qlik Sense")

def close_connection(connection):
    connection.close()
    print("Qlik Sense connection closed")
