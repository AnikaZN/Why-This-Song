import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

client_credentials_manager = SpotifyClientCredentials(client_id='CLIENT_ID',
                                       client_secret='CLIENT_SECRET')
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
