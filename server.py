from apiclient.discovery import build
import flask, requests, json
from flask import request, jsonify

my_api_key = "your-api-key"
my_cse_id = "your-cse-id"

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Live without Google</h1>'''

@app.route('/api/search', methods=['GET'])
def search():
    args = request.args
    return jsonify(google_search(args['term'], my_api_key, my_cse_id))
app.run()
