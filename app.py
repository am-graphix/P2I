import flask
from flask import jsonify
from fingerprint import Biometrics


app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/test')
def test_backend():
    print("Instruction received...")
    a = Biometrics()
    res = a.test_function()
    print(res)
    return jsonify({
        "message" : res
    })


if __name__ == '__main__':
    app.run(debug=True)