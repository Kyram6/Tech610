import requests
from pprint import pprint

from Requests.making_requests import response

POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"
# constant string (URL) - postcode added on later (that can change)

def postcode_lookup(postcode):
    response = requests.get(POSTCODE_ENDPOINT + postcode) #get request to api - joins URL + postcode

    print(response)

    if response.status_code == 200: # if request is ok
        response_json = response.json() # converts json format into python
        result = response_json["result"] #python reads whats in result key
        nhs_region =response_json["result"]["codes"]["nhs_region"]
        #dictionary in dict in dict
        #going into the first then the next so on so forth


        latitude = result["latitude"]
        longitude = result["longitude"]

        pprint((f"Postcode: {postcode}")) # pprint formats better
        pprint((f"Latitude: {latitude}"))
        pprint((f"Longitude: {longitude}"))
        pprint(f"NHS Region: {nhs_region}")

    else:
        print((f"404:ERROR"))


postcode_lookup("L40 9SB")





