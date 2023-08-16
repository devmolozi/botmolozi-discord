from flask import Flask
from threading import Thread

app = Flask('')
def home():
    return "i'm alive"

def run():
    app.run(host='files.000webhost.com', port=21)

def keep_alive():
    t = Thread(target=run)
    t.start()
