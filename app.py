from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    x = 0
    for i in range(1,90000000):
        x = x+1
        x = x-1
    return 'Hello, World!'


if __name__ == "__main__":
    app.run('0.0.0.0',port=5000,debug=True,threaded=True)