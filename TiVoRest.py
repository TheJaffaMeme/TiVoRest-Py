import flask
from flask import request
from pytivo import tivo_client
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = False

with open('config.json') as data_file:
    config = json.load(data_file)

TIVOIP = config['TIVOIP']
TIVOPORT = config['TIVOPORT']
HTTPIP = config['HTTPIP']
HTTPPORT = config['HTTPPORT']

## Set TiVo Box IP And Port
host = TIVOIP
port = TIVOPORT

tc = tivo_client.TivoClient(host, port)

@app.route('/IRCODE', methods=['GET'])
def ircode():
    value = request.args.get('value')
    tc.sendIRCode(value)
    return ('', 200)

@app.route('/SETCH', methods=['GET'])
def setch():
    value = request.args.get('value')
    tc.setChannel(value)
    return ('', 200)

@app.route('/STATUS', methods=['GET'])
def status():
    return (tc.getStatus(), 200)

app.run(host=HTTPIP, port=HTTPPORT)
