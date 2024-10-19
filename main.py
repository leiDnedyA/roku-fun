import argparse
import requests
from util.attack_on_titan import launch_attach_on_titan
from util.roku_connection import scan_roku_ip, test_connection
from util.roku_commands import keypress, launch_disney_plus
from flask import Flask, request, jsonify, render_template

roku_ip = None
app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return app.send_static_file(path)

@app.route('/attack-on-titan', methods=['POST'])
def attack_on_titan():
    if roku_ip:
        launch_attach_on_titan(roku_ip)
        return jsonify({"message": "SASAGEO SASAGEO"})
    else:
        return jsonify({"message": "unable to connect to roku device :("})

if __name__ == '__main__':
    roku_ip = scan_roku_ip()
    connection_successful = test_connection(roku_ip)

    if not connection_successful:
        print(f"ERROR: connection test failed. Attempted to connect to IP: \"{roku_ip}\"")

    app.run(host='0.0.0.0', port=5000)
