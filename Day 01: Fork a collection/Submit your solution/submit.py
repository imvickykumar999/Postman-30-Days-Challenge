import requests

url = "https://postman-echo.com/get?user-agent=PostmanRuntime/7.30.0"

payload = ""
headers = {
  'Cookie': 'sails.sid=s%3AmYXll3c6Pm13LjQ3SihgHM3G0NR2ZlZq.yk1d%2BHZrknCGRSc9MIqJy08bnAFJeOgZDGVfiRBZ7ls'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
