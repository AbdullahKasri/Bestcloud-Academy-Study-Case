from flask import *
import json, time

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'name': 'Abdullah', 'surname': 'KASRI'}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/city/', methods = ['GET'])
def request_page():
    user_query = str(request.args.get('city')) # /user/?=USER_NAME

    data_set = {'city': 'adana', 'temperature': '5'}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run(port = 8000, host = '0.0.0.0')