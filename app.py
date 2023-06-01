from flask import Flask,redirect,abort,make_response
import random

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/api/v2/zdd')
# Maintain compatibility with original version of 188api

@app.route('/api/v2/<string:name>')
def getmsg(name):
    try:
        text = open("text/"+name+".txt", encoding='utf-8')
    except FileNotFoundError:
        abort(404)
# Check if file exist
    else:
        msg = text.readlines()
        text.close()
        response = make_response(random.choice(msg))
        response.mimetype = 'text/plain'
# Set MIME
        return response
# Random select one line and return it

if __name__ == '__main__':
    app.run()
