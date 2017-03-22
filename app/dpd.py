#dpd server
import requests
import base64
import json

PDP_SERVER_URL='https://localhost:9443/api/identity/entitlement/decision/pdp'
USERNAME='admin'
PASSWORD='admin'

requests.packages.urllib3.disable_warnings()
url = PDP_SERVER_URL
username=USERNAME
password=PASSWORD
headers={'Authorization': 'Basic ' + base64.b64encode(username+':'+password),
             'Content-Type': 'application/json','Accept':'application/json'}




