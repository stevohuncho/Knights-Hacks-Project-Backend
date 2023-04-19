
# import libraries
from flask import Flask, request

# import functions from scrape.py
from scrape import getRestaurantsData, getRestaurantData, getMoreRestaurantData

server = Flask(__name__)

# hellow world route for an example
@server.route("/hello", methods=["GET"])
def hello():
    return "hello", 200

# gets restaurants data near user
@server.route("/nearme", methods=["GET"])
def nearme():
    # get latitude and longitude from query params
    latParams = request.args.getlist('lat')
    longParams = request.args.getlist('long')
    minPriceParams = request.args.getlist('min')
    maxPriceParams = request.args.getlist('max')
    milesParams = request.args.getlist('miles')

    # check if params are valid
    if len(latParams) != 1 or len(longParams) != 1 or len(minPriceParams) != 1 or len(maxPriceParams) != 1 or len(milesParams) !=1:
        return "insufficient or excessive query params", 400
    minPrice = int(minPriceParams[0])
    maxPrice = int(maxPriceParams[0])
    if maxPrice < minPrice or maxPrice < 0 or maxPrice > 4 or minPrice < 0 or minPrice > 4:
        return "invalid price range", 400

    # get data
    restaurantsData = getRestaurantsData(latParams[0], longParams[0], minPriceParams[0], maxPriceParams[0], milesParams[0])

    # check if response is valid
    if restaurantsData:
        return restaurantsData, 200

    # invalid response
    return "error while finding restaurant data", 400

# gets next page of restuarant data
@server.route("/nextPage", methods=["GET"])
def nextPage():
    # get latitude and longitude from query params
    latParams = request.args.getlist('lat')
    longParams = request.args.getlist('long')
    nextPageParams = request.args.getlist('token')


    # check if params are valid
    if len(latParams) != 1 or len(longParams) != 1 or len(nextPageParams) != 1:
        return "insufficient or excessive query params", 400

    # get data
    restaurantsData = getMoreRestaurantData(latParams[0], longParams[0], nextPageParams[0])

    # check if response is valid
    if restaurantsData:
        return restaurantsData, 200

    # invalid response
    return "error while finding restaurant data", 400

# get restaurant data in depth
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