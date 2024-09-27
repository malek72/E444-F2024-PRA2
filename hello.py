# Citation: "Flask Web Development : Developing Web Applications with Python Book Cover Image"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


