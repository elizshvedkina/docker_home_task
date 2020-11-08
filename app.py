import redis
from flask import Flask
from flask import Response


app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379)


@app.route('/')
def data():
    return_dict = {}
    for key in r.keys():
        return_dict[key.decode("utf-8")] = int(r.get(key).decode("utf-8"))
    return return_dict


@app.route('/health')
def hello():
    r = Response(response="RESPONSE STATUS 200", status=200)
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
