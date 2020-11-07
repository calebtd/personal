from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    exec(open("B5/B5.11_escapeRoom.py").read())


if __name__ == '__main__':
    port = 8000  # the custom port you want
    app.run(host='localhost', port=port)
