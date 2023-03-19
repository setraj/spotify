import requests
from services import auth
def getSongList():
        token = auth.getAuthToken()["access_token"]
        print(token)
        return token