from flask import Flask, request
from services import spotifyService
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hi():
    return "hi buddy!!"

@app.route('/v1/artists/<id>/top-songs', methods=['GET'])
def getSongs(id):
    market = request.args['market']
    if market == None:
        return "market is mandatory", 400
    return spotifyService.getSongList(id,market)