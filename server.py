# import libraries
from flask import Flask, request

# import functions from scrape.py
from scrape import scrapeRestaurantData

server = Flask(__name__)

# hellow world route for an example
@server.route("/hello", methods=["GET"])
def hello():
    return "hello", 200

# webscrape all restaurant data near a users location
@server.route("/scrape", methods=["GET"])
def scrape():
    # get latitude and longitude from query params
    latParams = request.args.getlist('lat')
    longParams = request.args.getlist('long')

    # check if params are valid
    if len(latParams) != 1 or len(longParams) != 1:
        return "insufficient or excessive query params", 400

    scrapeRestaurantData(latParams[0], longParams[0])

    return "success", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5001)