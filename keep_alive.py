from flask import Flask
from threading import Thread

app = Flask('')
def home():
    return "i'm alive"

def run():
    app.run(host='https://botmolozidc.netlify.app/', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
