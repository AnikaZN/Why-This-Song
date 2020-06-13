from flask import Flask, render_template
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

credentials = SpotifyClientCredentials(client_id='CLIENT_ID',
                                       client_secret='CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=credentials)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', title='Why This Song?')

if __name__ == '__main__':
    app.run()
