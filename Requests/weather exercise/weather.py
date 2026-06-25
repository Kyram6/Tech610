import requests
import sys

POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"
# constant string (URL) - postcode added on later (that can change)

def postcode_lookup(postcode):
    response = requests.get(POSTCODE_ENDPOINT + postcode) #get request to api - joins URL + postcode

    if response.status_code == 200: # if request is ok
        response_json = response.json() # convert json format into python dict
        result = response_json["result"] #python reads whats in result key

        latitude = result["latitude"] #gets lat and long from result
        longitude = result["longitude"]

        return latitude, longitude

    else:
        print((f"ERROR: Postcode not found")) #error message if postcode lookup fails
        return None

###################################
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?" # constant string
def get_weather(latitude, longitude): #get weather data using lat and long

    with open("weather_api_key") as file: #open file with api key
        api_key = file.readline().strip() #more secure

    response = requests.get(WEATHER_ENDPOINT +f"lat={latitude}&lon={longitude}&appid={api_key}&units=metric")
    #api request and send get request - units changed to metric at the end

    if response.status_code == 200: #checks weather request successful
        weather = response.json() # converts json into python dict
        return weather

    else:
        print("ERROR retrieving weather data.") #error message if weather data cant be retrieved
        return None

##################

#postcode = input("Enter a UK postcode:") #input =
#asks user to enter postcode

if len(sys.argv) < 2: #if less than 2 args then fails
    print(("Use: python weather.py <postcode>"))
    sys.exit(1) #error

postcode = sys.argv[1] #first arg after script name = postcode
coordinates= postcode_lookup(postcode) #looks up coordinates
weather = None #set variable so doesnt crash

if coordinates: #continue if postcode lookup successful
    latitude, longitude = coordinates #
    weather = get_weather(latitude, longitude)

if weather: #continue if weather data retrieved successfully
    location = weather["name"]
    temperature = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"] ##dictionary in dict in dict
    humidity = weather["main"]["humidity"]
    description = weather["weather"][0]["description"]
#extracts all the data we need ^^^

    print("Weather Report")
    print(f"Region - {location}")
    print(f"Temperature - {temperature}°C")
    print(f"Feels Like - {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description}")








