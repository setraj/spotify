import requests
from clients import spotifyClient
from services import auth
def getSongList(id,market):
        resp = spotifyClient.getTopSongsByArtist(id,market)
        return resp.json()