
import requests, json

#welcome_message = "Welcome Message"


def getZipCode():
	zipcode =  input("Please enter a 5 digit Zip Code: ")
	while len(zipcode) == 5:
			zipcode = zipcode
			break

	else:
		zipcode = input("Oops! You did not enter a valid zip code. Please enter a valid zip code: ")
		
	return zipcode

zipcode = getZipCode()

def create_url():
	full_url = ""
	url = "api.openweathermap.org/data/2.5/forecast?zip="
	api = "e4f9c3989f6e3d0f337d8f18c8995bef"
	
	full_url = url + zipcode + ",us&appid=" + api

	return full_url

full_url = create_url()

create_url()

req = requests.get(full_url)
wx = req.json()

#if connection successful, print wx
#if unsuccessful say try again, if still having erros, try later