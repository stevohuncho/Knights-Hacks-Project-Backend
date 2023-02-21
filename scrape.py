import requests, json

GOOGLE_API_KEY = "AIzaSyB20YZc6AgHLRGBTcWxxU1qCl7V5F2DF2w"

def getRestaurantsData(lat, long):
    # send request
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{long}&radius=1500&type=restaurant&key={GOOGLE_API_KEY}'
    response = requests.get(url)

    # check for errors
    if response.status_code != 200:
        print(f'ERROR: nearby search request statuscode:{response.status_code}')
        return 
    if len(response.text) == 0:
        print(f'ERROR: nearby search request statuscode:{response.status_code} empty body')
        return

    # parse response
    restaurantsData = {}
    responseJson = response.json()
    restaurantsData['next_page_token'] = responseJson['next_page_token']
    for location in responseJson['results']:
        locationData = {}
        locationData['price_level'] = location.get('price_level', None)
        locationData['rating'] = location.get('rating', None)
        locationData['num_of_ratings'] = location.get('user_ratings_total', None)
        locationData['keywords'] = location.get('types', None)
        locationData['address'] = location.get('vicinity', None)
        locationData['id'] = location.get('reference', None)
        restaurantsData[location['name']] = locationData
    return json.dumps(restaurantsData)
    
def getRestaurantData(id):
    # send request
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={id}&fields=formatted_phone_number%2Copening_hours%2Cwebsite%2Curl%2Ceditorial_summary%2Cdelivery%2Cdine_in%2Cformatted_address%2Ccurbside_pickup%2Cphotos%2Cserves_breakfast%2Cserves_brunch%2Cserves_lunch%2Cserves_dinner%2Cserves_vegetarian_food%2Cserves_wine%2Cserves_beer%2Ctakeout&key={GOOGLE_API_KEY}'
    response = requests.get(url)

    # check for errors
    if response.status_code != 200:
        print(f'ERROR: nearby search request statuscode:{response.status_code}')
        return 
    if len(response.text) == 0:
        print(f'ERROR: nearby search request statuscode:{response.status_code} empty body')
        return
    responseJson = response.json()
    if responseJson['status'] != "OK":
        status = responseJson.get('status', None)
        print(f'ERROR: nearby search request statuscode:{response.status_code} invalid status {status}')
        return
    
    # parse response
    print(response.json())
    return response.json()['result']
    