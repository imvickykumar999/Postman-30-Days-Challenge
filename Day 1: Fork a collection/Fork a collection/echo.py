
# https://www.postman.com/vickykumar999/workspace/github/request/21969867-c4ec287f-318d-48ac-a85d-89b788ed197b

import requests
import json

url = "https://postman-echo.com/post"

payload = json.dumps({
  "payload": "hello world"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
