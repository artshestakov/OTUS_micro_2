import json

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def hello_get():
    return json.dumps({"status": "OK"})


if __name__ == '__main__':
    app.run(port=8000)
