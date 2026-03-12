import requests
import base64

def solve(f):
	with open(f, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read()).decode('ascii')
		url = 'https://api.apitruecaptcha.org/one/gettext'

		data = { 
			'userid':'automate', 
			'apikey':'YmDhtLO8rniRGnA6acfi',  
			'data':encoded_string
		}
		response = requests.post(url = url, json = data)
		data = response.json()
		return data
	
solved = solve("captcha_images/captcha-img5.jpg")
print(solved)