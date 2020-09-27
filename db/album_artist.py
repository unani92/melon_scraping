from db.scrap_for_db import scrap_artist
import json

with open('album_songs.json') as album_songs:
    album_songs = json.load(album_songs)

with open('artist.json') as prev_artist:
    prev_artist = json.load(prev_artist)

prev_albums_num = [album['pk'] for album in prev_artist]
album_songs_artist_num = {artist for song in album_songs for artist in song['fields']['artist']}
new = [num for num in album_songs_artist_num if num not in prev_albums_num]

new_artists = scrap_artist(new)
new_artists += prev_artist

album_artists_file = open('album_artist.json', 'w+')
album_artists_file.write(json.dumps(new_artists))
