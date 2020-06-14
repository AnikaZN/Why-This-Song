from flask import Flask, render_template, session, request, redirect
from flask_session import Session
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

# app = Flask(__name__)
#
# credentials = SpotifyClientCredentials(client_id='CLIENT_ID',
#                                        client_secret='CLIENT_SECRET')
# sp = spotipy.Spotify(client_credentials_manager=credentials)
#
# @app.route('/', methods=['GET'])
# def index():
#     return 'Success!'
#
# if __name__ == '__main__':
#     app.run()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

auth_manager = spotipy.oauth2.SpotifyOAuth('CLIENT_ID', 'CLIENT_SECRET')
spotify = spotipy.Spotify(auth_manager=auth_manager)


@app.route('/')
def index():
    if request.args.get("code"):
        session['token_info'] = auth_manager.get_access_token(request.args["code"])
        return redirect('/')

    if not session.get('token_info'):
        auth_url = auth_manager.get_authorize_url()
        return f'<h2><a href="{auth_url}">Sign in</a></h2>'

    return f'<h2>Hi {spotify.me()["display_name"]}, ' \
           f'<small><a href="/sign_out">[sign out]<a/></small></h2>' \
           f'<a href="/playlists">My Playlists</a>'


@app.route('/sign_out')
def sign_out():
    session.clear()
    return redirect('/')


@app.route('/playlists')
def playlists():
    if not session.get('token_info'):
        return redirect('/')
    else:
        return spotify.current_user_playlists()
