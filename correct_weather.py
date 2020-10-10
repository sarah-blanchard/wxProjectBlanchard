import requests, json


degree_sign= u'\N{DEGREE SIGN}'

def show_Main_Menu():
	print('Welcome to WEATHER NOW')
	print('1 - Find current weather for a specific location')
	print('2 - Quit')

	return int(input('What would you like to do? '))


def getZipCode():
	zipcode =  input("Please enter a 5 digit Zip Code: ")
	while len(zipcode) == 5:
			zipcode = zipcode
			break

	else:
		zipcode = input("Oops! You did not enter a valid zip code. Please enter a valid zip code: ")
		
	return zipcode


def create_url():
	full_url = ""
	url = "http://api.openweathermap.org/data/2.5/weather?zip="
	zipcode = getZipCode()
	api = "e4f9c3989f6e3d0f337d8f18c8995bef"
	
	full_url = url + zipcode + "&units=imperial&us&appid=" + api

	return full_url


def get_weather():
	full_url = create_url()
	req = requests.get(full_url)
	wx = req.json()

	if wx["cod"] != "404": 
    
		location_name = wx["name"]

		tempDetails = wx["main"]
		current_temperature = tempDetails["temp"] 
		current_humidiy = tempDetails["humidity"] 
		current_pressure = tempDetails["pressure"] 

		windDetails = wx["wind"]
		current_wind = windDetails["speed"]
    
		current_statement = wx["weather"] 
		weather_description = current_statement[0]["description"] 

		print("Current weather for " + location_name + ": " + str(weather_description) +
	    	"\n Temperature: " + str(current_temperature) + degree_sign + "F" +
			"\n Humidity: " + str(current_humidiy) + "%" +
			"\n Wind: " + str(current_wind) + "mph" +
			"\n Atmospheric Pressure: " + str(current_pressure) + " hPa")

	else: 
		print("An unexpected error has occured, please ensure you have entered the correct zip code and try again") 
		show_Main_Menu()


def run_Weather():
	while (True):
		menu_option = show_Main_Menu()

		if (menu_option == 1):
			your_weather = get_weather()
			print(your_weather)

		elif (menu_option == 2):
			print('Thank you! See you soon!')
			break
		
		else:
			print('Please select a valid option')

		input('Press enter to return to the Menu')
	

run_Weather()

#if connection successful, print wx
#would you like to see the weather for another location?
#yes, loop, no, goodbye
#if unsuccessful say try again, if still having erros, try later
#loop to beginning

