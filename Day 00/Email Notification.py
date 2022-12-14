
# https://www.postman.com/vickykumar999/workspace/github/request/21969867-18ca00b9-68c4-4a22-88ee-a2c76f791e7b

import requests

url = "https://postman-echo.com/post?set_start_day=December 14, 2022"

payload={}
headers = {
  'Cookie': 'sails.sid=s%3Ae9FmX4cl50eDKu2PqELWG5KkAS1w1pn0.KKZUEo25zZW%2FTfAt%2BuIg9yGv4SlYLiwYC0DnZUmjI4U'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
