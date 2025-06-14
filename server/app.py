from flask import Flask, request
from server.core import get_default_json

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/get_json", methods=["GET"])
def get_json():
    print("Received request on 'get_json' endpoint")
    return get_default_json()


@app.route("/post_json", methods=["POST"])
def post_json():
    print("Received request on 'post_json' endpoint")
    json = get_default_json()
    json["input"] = request.json
    return json

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)