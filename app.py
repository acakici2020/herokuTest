import json
import time
from flask import Flask,request, jsonify

app = Flask(__name__)
queue = []

@app.route('/')
def index():
  return "<h1>Stonks Crpyto bot...</h1>"


@app.route("/webhook", methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        print(data)
        queue.append(data)
    except:
        pass
    res = {"message": "success"}
    return jsonify(res)


@app.route("/remove", methods=['POST'])
def remove():
    try:
        data = json.loads(request.data)
        print(data)
        for item in queue:
            try:
                if item["symbol"] == data["symbol"]:
                    queue.remove(item)
            except:
                pass
        # queue.append(data)
    except:
        pass
    res = {"message": "success"}
    return jsonify(res)




@app.route("/signals", methods=['GET'])
def signals():
    res = {"data": queue}
    return jsonify(res)


if __name__ == '__main__':
    app.run()
