from bs4 import BeautifulSoup
import requests
from db.scrap_for_db import scrap_album_song
import json

with open('album_songs.json') as album_songs:
    album_songs = json.load(album_songs)

with open('song_num.json') as song_num:
    song_num = json.load(song_num)

a_songs = scrap_album_song(song_num[1930:])

album_songs += a_songs

album_songs_file = open('album_songs.json',"w+")
album_songs_file.write(json.dumps(album_songs))