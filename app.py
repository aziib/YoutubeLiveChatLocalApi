from flask import Flask, jsonify
from flask_caching import Cache
from flask_cors import CORS
import json
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

def read_chat_data():
    while True:
        try:
            with open('chat_saved.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("chat_saved.json not found. Retrying in 1 second...")
            time.sleep(1)

@app.route('/chat')
@cache.cached(timeout=5)  # Cache the result for 5 seconds
def get_chat_output():
    chat_data = read_chat_data()
    return jsonify(chat_data)

if __name__ == '__main__':
    app.run(debug=False, port=5006)
