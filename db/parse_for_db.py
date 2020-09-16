from bs4 import BeautifulSoup
import requests
from db.scrap_for_db import scrap_song, scrap_artist, scrap_album
from db.auth_cookie import auth_cookie
from pprint import pprint
import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}
cookie = auth_cookie()
# 장르 바뀌면 장르코드 바꿔줘야됨!!!!!!!
def bs(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko",
        "Referer": "https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&steadyYn=Y",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": cookie
    }
    # header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}
    html = requests.get(url, headers=header).text
    bs = BeautifulSoup(html, 'html.parser')
    return bs.select('tr')[1:]

# # 음악 스크래핑
# ballad_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0100&steadyYn=Y')
# ballad1 = scrap_song(ballad_steady1)
# print('fin ballad1 bs')
#
# ballad_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=200&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad2 = scrap_song(ballad_steady2)
# print('fin ballad2 bs')

with open('./db/song.json') as song_file:
    songs = json.load(song_file)

# ballad_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad3 = scrap_song(ballad_steady3)
# print('fin ballad3 bs')
#
# ballad_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad4 = scrap_song(ballad_steady4)
# print('fin ballad4 bs')
#
# ballad_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad5 = scrap_song(ballad_steady5)
# print('fin ballad5 bs')

# ballad_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad6 = scrap_song(ballad_steady6)
# print('fin ballad6 bs')
#
# ballad_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad7 = scrap_song(ballad_steady7)
# print('fin ballad7 bs')

# ballad_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad8 = scrap_song(ballad_steady8)
# print('fin ballad8 bs')
#
# ballad_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad9 = scrap_song(ballad_steady9)
# print('fin ballad9 bs')


# ballad_steady10 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=451&pageSize=50&gnrCode=GN0100&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# ballad10 = scrap_song(ballad_steady10)
# print('fin ballad10 bs')


# rnb_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0400&steadyYn=Y')
# rnb1 = scrap_song(rnb_steady1)
# print('fin rnb1 bs')
#
# rnb_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb2 = scrap_song(rnb_steady2)
# print('fin rnb2 bs')

#
#
# rnb_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb3 = scrap_song(rnb_steady3)
# print('fin rnb3 bs')
#
# rnb_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb4 = scrap_song(rnb_steady4)
# print('fin rnb4 bs')
#
# rnb_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb5 = scrap_song(rnb_steady5)
# print('fin rnb5 bs')
#
# rnb_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb6 = scrap_song(rnb_steady6)
# print('fin rnb6 bs')

# rnb_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb7 = scrap_song(rnb_steady7)
# print('fin rnb7 bs')
#
# rnb_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb8 = scrap_song(rnb_steady8)
# print('fin rnb8 bs')
#

# rnb_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb9 = scrap_song(rnb_steady9)
# print('fin rnb6 bs')
#
# rnb_steady10 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=451&pageSize=50&gnrCode=GN0400&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rnb10 = scrap_song(rnb_steady10)
# print('fin rnb10 bs')

# indie_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0500&steadyYn=Y')
# indie1 = scrap_song(indie_steady1)
# print('fin indie1 bs')
#
# indie_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie2 = scrap_song(indie_steady2)
# print('fin indie2 bs')
#
# indie_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie3 = scrap_song(indie_steady3)
# print('fin indie3 bs')
#
# indie_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie4 = scrap_song(indie_steady4)
# print('fin indie4 bs')
#

# indie_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie5 = scrap_song(indie_steady5)
# print('fin indie5 bs')
#
# indie_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie6 = scrap_song(indie_steady6)
# print('fin indie6 bs')
#
# indie_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie7 = scrap_song(indie_steady7)
# print('fin indie7 bs')
#

# indie_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie8 = scrap_song(indie_steady8)
# print('fin indie8 bs')
#
# indie_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie9 = scrap_song(indie_steady9)
# print('fin indie9 bs')
#
# indie_steady10 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=451&pageSize=50&gnrCode=GN0500&dtlGnrCode=GN0501&orderBy=NEW&steadyYn=Y')
# indie10 = scrap_song(indie_steady10)
# print('fin indie10 bs')

# rock_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0600&steadyYn=Y')
# rock1 = scrap_song(rock_steady1)
# print('fin rock1 bs')
#
# rock_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock2 = scrap_song(rock_steady2)
# print('fin rock2 bs')
#
# rock_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock3 = scrap_song(rock_steady3)
# print('fin rock3 bs')

# rock_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock4 = scrap_song(rock_steady4)
# print('fin rock4 bs')
#
# rock_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock5 = scrap_song(rock_steady5)
# print('fin rock5 bs')
#
# rock_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock6 = scrap_song(rock_steady6)
# print('fin rock6 bs')

# rock_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock7 = scrap_song(rock_steady7)
# print('fin rock7 bs')
#
# rock_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock8 = scrap_song(rock_steady8)
# print('fin rock8 bs')
#
# rock_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock9 = scrap_song(rock_steady9)
# print('fin rock9 bs')

# rock_steady10 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=451&pageSize=50&gnrCode=GN0600&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rock10 = scrap_song(rock_steady10)
# print('fin rock10 bs')

# dance_steady = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0200&steadyYn=Y')
# dance1 = scrap_song(dance_steady)
# print('fin dance1 bs')
#
# dance_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance2 = scrap_song(dance_steady2)
# print('fin dance2 bs')
#
# dance_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance3 = scrap_song(dance_steady3)
# print('fin dance3 bs')
#
# dance_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance4 = scrap_song(dance_steady4)
# print('fin dance4 bs')

# dance_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance5 = scrap_song(dance_steady5)
# print('fin dance5 bs')
#
# dance_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance6 = scrap_song(dance_steady6)
# print('fin dance6 bs')
#
# dance_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance7 = scrap_song(dance_steady7)
# print('fin dance7 bs')

# dance_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance8 = scrap_song(dance_steady8)
# print('fin dance8 bs')
#
# dance_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance9 = scrap_song(dance_steady9)
# print('fin dance9 bs')
#
# dance_steady10 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=451&pageSize=50&gnrCode=GN0200&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# dance10 = scrap_song(dance_steady10)
# print('fin dance10 bs')

# rap_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0300&steadyYn=Y')
# rap1 = scrap_song(rap_steady1)
# print('fin rap1 bs')

# rap_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap2 = scrap_song(rap_steady2)
# print('fin rap2 bs')
#
# rap_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap3 = scrap_song(rap_steady3)
# print('fin rap3 bs')
#
# rap_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap4 = scrap_song(rap_steady4)
# print('fin rap4 bs')
#
# rap_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap5 = scrap_song(rap_steady5)
# print('fin rap5 bs')

# rap_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap6 = scrap_song(rap_steady6)
# print('fin rap6 bs')
#
# rap_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap7 = scrap_song(rap_steady7)
# print('fin rap7 bs')
#
# rap_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap8 = scrap_song(rap_steady8)
# print('fin rap8 bs')
#
# rap_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0300&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# rap9 = scrap_song(rap_steady9)
# print('fin rap9 bs')

# folk_steady1 = bs('https://www.melon.com/genre/song_list.htm?gnrCode=GN0800&steadyYn=Y')
# folk1 = scrap_song(folk_steady1)
# print('fin folk1 bs')
#
# folk_steady2 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=51&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk2 = scrap_song(folk_steady2)
# print('fin folk2 bs')
#
# folk_steady3 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=101&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk3 = scrap_song(folk_steady3)
# print('fin folk3 bs')
#
# folk_steady4 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=151&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk4 = scrap_song(folk_steady4)
# print('fin folk4 bs')

# folk_steady5 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=201&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk5 = scrap_song(folk_steady5)
# print('fin folk5 bs')
#
# folk_steady6 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=251&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk6 = scrap_song(folk_steady6)
# print('fin folk6 bs')
#
# folk_steady7 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=301&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
# folk7 = scrap_song(folk_steady7)
# print('fin folk7 bs')

folk_steady8 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=351&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
folk8 = scrap_song(folk_steady8)
print('fin folk8 bs')

folk_steady9 = bs('https://www.melon.com/genre/song_listPaging.htm?startIndex=401&pageSize=50&gnrCode=GN0800&dtlGnrCode=&orderBy=NEW&steadyYn=Y')
folk9 = scrap_song(folk_steady9)
print('fin folk9 bs')

songs += folk8 + folk9

# 중복 제거 및 중복여부 검증
songs = list({v['pk']:v for v in songs}.values())
song_file = open("./db/song.json", "w+")
song_file.write(json.dumps(songs))

print(len(songs))

# song_file = open("./db/song.json", "w+")
# song_file.write(json.dumps(songs))

# # 스크래핑된 음악의 가수 스크래핑
# artists = set()
# for song in songs:
#     musicians = song['fields']['artist']
#     for m in musicians:
#         artists.add(m)
# artists = list(artists)
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
# artists = scrap_artist(artists) + [various_artist]
# artist_file = open('./db/artist.json',"w+")
# artist_file.write(json.dumps(artists))
#
# # 스크래핑된 음악의 앨범 스크래핑
# albums = set()
# for song in songs:
#     album_id = song['fields']['album']
#     albums.add(album_id)
# albums = list(albums)
#
# albums = scrap_album(albums)
# album_file = open('./db/album.json', 'w+')
# album_file.write(json.dumps(albums))
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

