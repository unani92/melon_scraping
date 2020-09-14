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

with open('song.json') as song_file:
    songs = json.load(song_file)

artists = set()
for song in songs:
    musicians = song['fields']['artist']
    for m in musicians:
        artists.add(m)
artists = list(artists)
print(len(artists))
