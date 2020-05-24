import requests
import json

class RequestBuilder():

    URL = 'blank'

    def __init__(self, url):
        self.URL = url

    def postRequest(self):
        headers = {'Content-Type': 'application/json'}

        payload = {'key1': 1, 'key2': 'value2'}

        resp = requests.post(self.URL, headers=headers, data=json.dumps(payload,indent=4))

        return resp
