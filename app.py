from flask import Flask
import os
import random

text = open("text.txt", encoding='utf-8')
msg = text.readlines()

app = Flask(__name__)


@app.route('/')
def getmsg():
    return random.choice(msg)


if __name__ == '__main__':
    app.run()
