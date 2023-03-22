from urllib.parse import quote
import requests
from services import auth
from configs import secrets

#curl -X "GET" "https://api.spotify.com/v1/artists/4gdMJYnopf2nEUcanAwstx/top-tracks?market=IN"
# -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQCgZ2-Kpe1HIXtJxshlHeS84jDozA0q_SGMZu3QKbRnMw1b7f4_lRZ2IhBtsMDXin0-SQj0oxjVNDZj5zow6wrw1VVylBePiUe59xWMeYsKcVTZjKtp"
#'https://api.spotify.com/v1/artists/{id}/top-tracks'

def getTopSongsByArtist(id, market):
    authToken = auth.getAuthToken()
    url = secrets.topSongsByArtistURL.format(quote(id))
    headers = {'Authorization': 'Bearer ' + authToken,
               'Content-Type':'application/json',
               'Accept':'application/json'}
    params = {'market': market}
    resp = requests.get(url,headers=headers,params=params)
    return resp