import requests
from clients import spotifyClient
from services import auth
def getSongList(id,market):
        resp = spotifyClient.getTopSongsByArtist(id,market)
        topSongsDect = resp.json()
        allTracks = topSongsDect['tracks']
        trackNames = []
        for track in allTracks:
                trackNames.append(track['name'])
        return trackNames