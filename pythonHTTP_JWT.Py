#code is similiar to a need I had at work - but i have taken all the biz specifics out... would like htis for reference use in future
#have not tested this since adoprting biz case to more agnostic case... just want all the peices here for usage in the future.. might need to debug a bit

import requests
import json

print ('imports complete\n')



#config info for auth
authentication_endpoint = 'https://somepage.com:80/api/auth'
authentication_json = {"username": "someuser", "password": "somepass"}



#config info for payload
payload_endpoint =  'https://somepage.com:80/api/payload'
payload_jsonFile = "C:/MyFile.Json"

with open(payload_jsonFile, encoding='utf-8-sig') as f:
    payload_jsonFile = json.load(f, strict=false)
print(f'File loaded ({payload_jsonFile})')




#Send out auth data
response_auth = requests.post(authentication_endpoint, json=authentication_json)



#Get JWT Token
jwtToken = ""
if response_auth.status_code = 200:
    jwtToken = response_auth.json()['token']
else:
    print(f'Error:  Unexpected Status Code "{response_auth.status_code}"')



##payload section
if jwtToken != "":
    print(f'JWT Token assigned: {jwtToken}\n')

    ##build http header using jwt token (take note of fstring syntax)
    httpHeader = {'Authorization': f'Bearer {jwtToken}'}
    
    
    response_payload = requests.post(payload_endpoint, headers = httpHeader, json = payload_jsonFile)
    print(f'Status Code: {response_payload.status_code}\n')


    print('response content:')
    print(response_inferHCC.content)


else:    
    print('you gotta problem')




