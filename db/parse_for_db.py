from bs4 import BeautifulSoup
import requests
from db.scrap_for_db import scrap_song, scrap_artist, scrap_album
from pprint import pprint

import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}

# 음악 스크래핑
love1_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=482499717', headers=header).text
love1_bs = BeautifulSoup(love1_html, "html.parser")
love_1 = love1_bs.select('tr')[1:]

songs = scrap_song(love_1)
song_file = open("./db/song.json", "w+")
song_file.write(json.dumps(songs))

with open('./db/song.json') as song_file:
    songs = json.load(song_file)

# 스크래핑된 음악의 가수 스크래핑
artists = set()
for song in songs:
    musicians = song['fields']['artist']
    for m in musicians:
        artists.add(m)
artists = list(artists)

various_artist = {
            'model': 'music.artist',
            'pk': 1,
            'fields': {
                'name': 'various artist',
                'img': '',
                'debue': '',
                'type': '',
                'member': 'members'
            }
        }

artists = scrap_artist(artists) + [various_artist]
artist_file = open('./db/artist.json',"w+")
artist_file.write(json.dumps(artists))

# 스크래핑된 음악의 앨범 스크래핑
albums = set()
for song in songs:
    album_id = song['fields']['album']
    albums.add(album_id)
albums = list(albums)

albums = scrap_album(albums)
album_file = open('./db/album.json', 'w+')
album_file.write(json.dumps(albums))

genres = set()
for song in songs:
    genre_name = song['fields']['genres']
    for g in genre_name:
        genres.add(g)

for album in albums:
    genre_name = album['fields']['genres']
    for g in genre_name:
        genres.add(g)

genre_lst = []
for idx, genre in enumerate(genres):
    genre_lst.append({
        'model': 'music.genre',
        'pk': genre,
        'fields': {
            'num': idx
        }
    })

genre_file = open('./db/genre.json', 'w+')
genre_file.write(json.dumps(genre_lst))

