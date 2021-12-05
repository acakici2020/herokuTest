import json
import time
from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
queue = []


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


@app.route("/signals", methods=['GET'])
def signals():
    res = {"data": queue}
    return jsonify(res)


if __name__ == '__main__':
    app.run()
