from flask import Flask

app = Flask(__name__)

from app import routes

app.run( port = 3000, debug = False)