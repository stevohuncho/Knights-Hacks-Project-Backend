from flask import Flask, request

server = Flask(__name__)

# hellow world route for an example
@server.route("/hello", methods=["GET"])
def hello():
    return "hello", 200

# webscrape all restaurant data near a users location
@server.route("/scrape", methods=["POST"])
def scrape():
    pass


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5001)