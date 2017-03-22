import requests
import base64
import json
import ast




requests.packages.urllib3.disable_warnings()
url='https://localhost:9443/api/identity/entitlement/decision/pdp'
headers={'Authorization': 'Basic ' + base64.b64encode('admin'+':'+'admin'),
             'Content-Type': 'application/json','Accept':'application/json'}
data='{"Request":{"Action":{"Attribute":[{"AttributeId":"urn:oasis:names:tc:xacml:1.0:action:action-id","Value":"read"}]},"Resource":{"Attribute":[{"AttributeId":"urn:oasis:names:tc:xacml:1.0:resource:resource-id","Value":"http://127.0.0.1/service/very_secure/"}]}}}'
print (data)
response = requests.post(url, data=data,headers=headers,verify=False)
print(response.text)



d=response.json()
d=d['Response'][0]['Decision']
print(d)
print(d == "Permit")


with open('xacml.req', 'r') as myfile:
    data=myfile.read().replace('\n', '')  
print (data)
response = requests.post(url, data=data,headers=headers,verify=False)
print(response.text)