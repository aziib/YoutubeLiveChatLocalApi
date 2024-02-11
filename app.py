from flask import Flask, jsonify
from flask_caching import Cache
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route('/chat')
@cache.cached(timeout=5)  # Cache the result for 60 seconds
def get_chat_output():
    with open('chat_saved.json', 'r') as file:
        chat_data = json.load(file)
    return jsonify(chat_data)

if __name__ == '__main__':
    app.run(debug=False, port=5006)
