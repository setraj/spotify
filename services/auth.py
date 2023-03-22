import requests
import base64
from configs import secrets

def getAuthToken():
    clientCreds = secrets.ClientID + ':' + secrets.ClientSecret
    clientCredsB64 = base64.b64encode(clientCreds.encode())
    token_data = {
        'grant_type': 'client_credentials'
    }
    headers = {'Authorization': 'Basic ' + clientCredsB64.decode(),
               'Content-Type':'application/x-www-form-urlencoded'}
    resp = requests.post(secrets.spotifyAuthURL,headers=headers,data=token_data)
    return resp.json()["access_token"]