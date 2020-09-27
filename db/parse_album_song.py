from bs4 import BeautifulSoup
import requests
from db.scrap_for_db import scrap_song, scrap_artist, scrap_album
from db.auth_cookie import auth_cookie
import re
# from db.cache import artists, albums
import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}
cookie = auth_cookie()

with open('album.json') as albums:
    albums = json.load(albums)

with open('song_num.json') as songs:
    songs = json.load(songs)

songs = list(set(songs))

album_id = [album['pk'] for album in albums]

song_num = []
for idx, pk in enumerate(album_id[1586:]):
    album_html = requests.get(f'https://www.melon.com/album/detail.htm?albumId={pk}', headers=header).text
    album_bs = BeautifulSoup(album_html, 'html.parser')
    
    try:
        tr_all = album_bs.find('tbody').select('tr')
    
        for tr in tr_all:
            try:
                if tr['class'][0] == 'cd':
                    continue
                else:
                    song = tr.find('a')['href']
                    song = int(re.findall('\d+', song)[0])
                    song_num.append(song)
            except KeyError:
                song = tr.find('a')['href']
                song = int(re.findall('\d+', song)[0])
                song_num.append(song)
        if not idx % 50:
            print(f'{1585 + idx} / {len(album_id)} fin')
    except:
        print(f'앨범 {1585 + idx - 1}/{len(album_id)}까지 하다 멈춤')
        break
        
songs += song_num

song_num_file = open('song_num.json',"w+")
song_num_file.write(json.dumps(songs))