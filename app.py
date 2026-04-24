import flask
from flask import jsonify
from fingerprint import Biometrics
import time


app = flask.Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/test')
def test_backend():
    print("Instruction received...")
    a = Biometrics()
    res = a.test_function()
    print(res)
    time.sleep(2)
    return jsonify({
        "message" : res
    })


if __name__ == '__main__':
    app.run(debug=True)