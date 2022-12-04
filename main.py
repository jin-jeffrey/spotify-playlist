from pynput.keyboard import Key, Listener
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
    tracks_added = []

    def on_press(key):
        if (key == start and token):
            # get current song and add it to playlist
            current_track = sp.current_user_playing_track()
            if (current_track):
                song_id = current_track['item']['id']
                song_name = current_track['item']['name']
                if (song_id not in tracks_added):
                    sp.user_playlist_add_tracks(username, playlist_id=playlist, tracks=[song_id])
                    tracks_added.append(song_id)
                    print(song_name + " added.")
        if (key == stop):
            print("Application stopped.")
            return False

    token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=secret, redirect_uri=redirect)
    if token:
        sp = spotipy.Spotify(auth=token)
        print("Application started.")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()