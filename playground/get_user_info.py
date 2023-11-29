import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "7777ac4f09a747a1ab0f0e1cef7a2323"
CLIENT_SECRET = "11cf4026d8084e4ca99081bb8c2f93cd"

# Set up Authorization
os.environ["SPOTIPY_CLIENT_ID"] = CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:9000"
scope = ["user-library-read user-library-modify playlist-modify-public"]

# Set up spotipy.client.Spotify object which is authenticated
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# print(type(sp))
user = sp.current_user()
# print(user)
# print(type(user))
# print("--User Info--")
# print("Name:", user["display_name"])
# print("Total followers:", user["followers"]["total"])

# Create playlist
# print(sp.user_playlist_create(user=user["id"], name="Test (2)", public=True, collaborative=False))
# print(type(sp.user_playlist_create(user=user["id"], name="Test (2)", public=True, collaborative=False)))

# print(sp.playlist_add_items(playlist_id="https://open.spotify.com/playlist/0y2bGYwNakOcgcDz5YshQR?si=8b8fd34eff74406d",
#                             items=["https://open.spotify.com/track/5xEM5hIgJ1jjgcEBfpkt2F?si=16c439f41fd14283"]))
# print(type(sp.playlist_add_items(playlist_id="https://open.spotify.com/playlist/0y2bGYwNakOcgcDz5YshQR?si=8b8fd34eff74406d",
#                                  items=["https://open.spotify.com/track/5xEM5hIgJ1jjgcEBfpkt2F?si=16c439f41fd14283"])))


daylist_url = "https://open.spotify.com/playlist/37i9dQZF1EP6YuccBxUcC1?si=f5d4859eafbd461c"
daylist_tracks = sp.playlist_items(playlist_id=daylist_url)
print(daylist_tracks.keys())
print(daylist_tracks["items"][0]["track"].keys())
for tracks in daylist_tracks["items"]:
    track = tracks["track"]
    print(track["name"])
    print(track["album"]["name"])
    print(track["artists"][0]["name"])
# print(daylist_tracks.get("items"))
# print(type(daylist_tracks))
# print(daylist_tracks.keys())
# print(type(daylist_tracks["items"][0].keys()))
# print(daylist_tracks["items"][0]["track"].keys())

#
# # Get User Playlist
# user_current_playlists = sp.current_user_playlists()
# print("--User Current Playlists---")
# print(user_current_playlists.keys())
# for playlist in user_current_playlists["items"]:
#     print("Playlist's name:", playlist["name"])
#     print("Playlist's ID:", playlist["id"])
#     print("Playlist's description:", playlist["description"])
#     print("Total tracks:", playlist["tracks"]["total"])
#     # print(playlist)
#     print("*")
#
#
# # Get User Current Saved Tracks
# user_current_saved_tracks = sp.current_user_saved_tracks(limit=10)
# print("--User Current Saved Tracks--")
# print(user_current_saved_tracks)
# print(user_current_saved_tracks["total"])
#
#
# # Print out first 10 current saved tracks
# print("First 10 current saved tracks")
# for i in range(len(user_current_saved_tracks["items"][:10])):
#     current_track = user_current_saved_tracks["items"][i]["track"]
#     print("Track's name:", current_track["name"])
#     print("Track's album:", current_track["album"]["name"])
#     print("Track's artist:", current_track["artists"][0]["name"])
#     print("*")
# print("---")
#
#
# # Get Weekly Discovery Playlist info
# weekly_playlist_url = "https://open.spotify.com/playlist/37i9dQZEVXcSl5JcFboUlo?si=105e91e417bc41a0"
# weekly_playlist = sp.playlist(playlist_id=weekly_playlist_url)
# print(weekly_playlist.keys())
# print(weekly_playlist["tracks"].keys())
# print(weekly_playlist["tracks"]["items"][0])
#
# for track in weekly_playlist["tracks"]["items"]:
#     track_info = track["track"]
#     print("Name:", track_info["name"])
#     print("Artist:", track_info["artists"][0]["name"])
#     print("Album:", track_info["album"]["name"])
#     print("*")


