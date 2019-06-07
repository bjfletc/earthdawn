# Flask Application for Earthdawn Sessions

from flask import Flask, render_template

earthdawn_app = Flask(__name__)

@earthdawn_app.route('/')
def index():
    return render_template('index.html')
