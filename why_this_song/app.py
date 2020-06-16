from flask import Flask, render_template, session, request, redirect
from flask_session import Session
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

client_credentials_manager = SpotifyClientCredentials(client_id='CLIENT_ID',
                                       client_secret='CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@app.route('/', methods=['GET'])
def index():
    return 'Success!'

@app.route('/track', methods=['GET', 'POST'])
def song():
    # spotipy.oauth2.SpotifyOauthError: Bad Request at this line
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])

if __name__ == '__main__':
    app.run()
