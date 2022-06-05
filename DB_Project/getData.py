import json
import requests
from getAccess import return_token

api_url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

access_token = return_token()

headers = {
  "Authorization": "Bearer {}".format(access_token),
  "Content-Type": "application/json;encoding=utf-8"
  }

dataTypesUrl = ["com.google.sleep.segment","com.google.step_count.delta","com.google.heart_rate.bpm"]

body = {
  "aggregateBy": [{
    "dataTypeName": "com.google.heart_rate.bpm"
  }],
  
  "startTimeMillis": 1649348039497,
  "endTimeMillis": 1650557611729
}


response = requests.post(api_url, data=json.dumps(body), headers=headers)

print(response.text)