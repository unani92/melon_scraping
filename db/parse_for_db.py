from bs4 import BeautifulSoup
import requests
from db.scrap_for_db import scrap_song, scrap_artist, scrap_album
from db.auth_cookie import auth_cookie
from db.cache import artists, albums
import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}
cookie = auth_cookie()
# 장르 바뀌면 장르코드 바꿔줘야됨!!!!!!!

# "Referer": "https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=479848178",
# "X-Requested-With": "XMLHttpRequest",
# "Cookie": cookie

def bs(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko",
        # "Referer": "https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=473654162",
        # "X-Requested-With": "XMLHttpRequest",
        # "Cookie": cookie
    }
    # header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    html = requests.get(url, headers=header).text
    bs = BeautifulSoup(html, 'html.parser')
    return bs.select('tr')[1:]

# 음악 스크래핑

with open('./db/song.json') as song_file:
    songs = json.load(song_file)

# sad1_bs = bs('https://www.melon.com/dj/playlist/djplaylist_listsong.htm?startIndex=51&pageSize=50&plylstSeq=473654162')
# sad1 = scrap_song(sad1_bs)
# print('sad bs fin')
#
# songs += sad1
#
# # 중복 제거 및 중복여부 검증
# songs = list({v['pk']:v for v in songs}.values())
# song_file = open("./db/song.json", "w+")
# song_file.write(json.dumps(songs))
#
# print(len(songs))

# song_file = open("./db/song.json", "w+")
# song_file.write(json.dumps(songs))

# 스크래핑된 음악의 가수 스크래핑
# artists_lst = artists()
#
# various_artist = {
#             'model': 'music.artist',
#             'pk': 1,
#             'fields': {
#                 'name': 'various artist',
#                 'img': '',
#                 'debue': '',
#                 'type': '',
#                 'member': 'members'
#             }
#         }
#
# artists_dicts = scrap_artist(artists_lst) + [various_artist]
# artist_file = open('./db/artist.json',"w+")
# artist_file.write(json.dumps(artists_dicts))

# 스크래핑된 음악의 앨범 스크래핑
albums_lst = albums()

albums = scrap_album(albums_lst)
album_file = open('./db/album.json', 'w+')
album_file.write(json.dumps(albums))
#
# genres = set()
# for song in songs:
#     genre_name = song['fields']['genres']
#     for g in genre_name:
#         genres.add(g)
#
# for album in albums:
#     genre_name = album['fields']['genres']
#     for g in genre_name:
#         genres.add(g)
#
# genre_lst = []
# for idx, genre in enumerate(genres):
#     genre_lst.append({
#         'model': 'music.genre',
#         'pk': genre,
#         'fields': {
#             'num': idx
#         }
#     })
#
# genre_file = open('./db/genre.json', 'w+')
# genre_file.write(json.dumps(genre_lst))

