from flask import Flask
from services import spotifyService
app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/songs/', methods=['GET'])
def getSongs():
    return spotifyService.getSongList()