from pynput.keyboard import Key, Listener
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import config

def main():

    start = Key.delete
    stop = Key.page_down
    playlist = config.PLAYLIST
    cid = config.CID
    secret = config.SECRET
    redirect = config.REDIRECT
    scope = config.SCOPE
    username = config.USERNAME

    def on_press(key):
        if (key == start and token):
            # get current song
            current_song = sp.current_user_playing_track()['item']['id']
            # add it to playlist
            sp.user_playlist_add_tracks(username, playlist_id=playlist, tracks=[current_song])
        if (key == stop):
            print("Application stopped.")
            return False

    token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect)
    if token:
        sp = spotipy.Spotify(auth=token)
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()