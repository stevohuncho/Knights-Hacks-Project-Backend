# import libraries
from flask import Flask, request

# import functions from scrape.py
from scrape import getRestaurantsData, getRestaurantData

server = Flask(__name__)

# hellow world route for an example
@server.route("/hello", methods=["GET"])
def hello():
    return "hello", 200

# gets restaurants data near user
# example http://localhost:5001/nearme?lat=28.5970378&long=-81.2276083
@server.route("/nearme", methods=["GET"])
def nearme():
    # get latitude and longitude from query params
    latParams = request.args.getlist('lat')
    longParams = request.args.getlist('long')

    # check if params are valid
    if len(latParams) != 1 or len(longParams) != 1:
        return "insufficient or excessive query params", 400

    # get data
    restaurantsData = getRestaurantsData(latParams[0], longParams[0])

    # check if response is valid
    if restaurantsData:
        return restaurantsData, 200

    # invalid response
    return "error while finding restaurant data"

# get restaurant data in depth
# example http://localhost:5001/restaurant?id=ChIJNX-91oxo54gRDzDmAJVGFRM
@server.route("/restaurant", methods=["GET"])
def restaurant():
    # get id from query params
    idParams = request.args.getlist('id')

    if len(idParams) != 1:
        return "insufficient or excessive query params", 400

    # get data
    restaurantData = getRestaurantData(idParams[0])

    # check if response is valid
    if restaurantData:
        return restaurantData, 200

    # invalid response
    return "error while finding restaurant data"



if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5001)