import requests
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/internal_url")
def internal_url():
    INTERNAL_URL = os.environ.get("INTERNAL_URL")

    r = requests.get(INTERNAL_URL)
    return jsonify({
        "Status_Code": r.status_code,
        "Response": r.text
    })

@app.route("/external_url")
def external_url():
    EXTERNAL_URL = os.environ.get("EXTERNAL_URL")

    r = requests.get(EXTERNAL_URL)
    return jsonify({
        "Status_Code": r.status_code,
        "Response": r.text
    })


if __name__ == "__main__":
    PORT = os.environ.get("PORT")
    app.run(host="0.0.0.0", port=PORT, threaded=True, debug=True)