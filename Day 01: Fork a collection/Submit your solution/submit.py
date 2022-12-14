
# https://www.postman.com/vickykumar999/workspace/github/request/21969867-c0935fb6-a93a-42fb-8b5a-b2380282a3f5

import requests

url = "https://postman-echo.com/get?user-agent=PostmanRuntime/7.30.0"

payload = ""
headers = {
  'Cookie': 'sails.sid=s%3AmYXll3c6Pm13LjQ3SihgHM3G0NR2ZlZq.yk1d%2BHZrknCGRSc9MIqJy08bnAFJeOgZDGVfiRBZ7ls'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
