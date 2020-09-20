# L=[
#     {'id':1,'name':'john', 'age':34},
#     {'id':1,'name':'john', 'age':34},
#     {'id':2,'name':'hanna', 'age':30},
# ]
#
# a = list({v['id']:v for v in L}.values())
# print(a)

import json
from pprint import pprint
from db.scrap_for_db import scrap_album

with open('album.json') as albums:
    albums = json.load(albums)

with open('song.json') as songs:
    songs = json.load(songs)

with open('artist.json') as artists:
    artists = json.load(artists)

artists = list({v['pk']:v for v in artists}.values())


# pprint(albums[20])
#
# artists = set()
# all = albums + songs
#
# for a in all:
#     temp = a['fields']['artist']
#     for t in temp:
#         artists.add(t)
#
# tt = set()
# for song in songs:
#     temp = song['fields']['artist']
#     for t in temp:
#         tt.add(t)
#
# print(len(list(tt)))
# print(len(list(artists)))
