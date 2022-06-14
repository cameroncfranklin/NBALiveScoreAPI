from flask import *
from flask_cors import CORS
import json
import time
import scraper

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def home_page():
    data_set = scraper.scraper()
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/request/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))  # /user/?user=USER_NAME

    data_set = {'Page': 'Request',
                'Message': f'Successfully got the request for {user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


def main():
    scraper()
    # refresh()


if __name__ == '__main__':
    app.run(port=7776)
    # main()
