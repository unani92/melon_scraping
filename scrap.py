from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}

def scrap(bs_object, emotion=None, header=None):
    if header is None:
        header = headers
    song_lst = []

    for song in bs_object:

        songId = song.find('a', class_='song_info')['href']
        songId = int(re.findall("\d+", songId)[0])

        song_res = requests.get(f'https://www.melon.com/song/detail.htm?songId={int(songId)}', headers=header).text
        bs = BeautifulSoup(song_res, 'html.parser')
        section_info = bs.find('div', class_='section_info')

        try:
            album_img = section_info.find('img')['src']
        except:
            album_img = ''

        song_name = section_info.find('div', class_='song_name')
        song_name = re.sub(r"\s+", " ", song_name.text.rstrip())[4:]

        # artist 2명 이상일수도 있음 조심
        artist_all = section_info.findAll('a', class_='artist_name')
        artist = []
        for a in artist_all:
            id = int(re.findall('\d+', a['href'])[0])
            name = a['title']
            artist.append({
                'id': id,
                'name': name
            })

        meta = section_info.select('.list dd')

        try:
            album_id = meta[0].find('a')['href']
            album_id = int(re.findall("\d+", album_id)[0])
        except:
            album_id = ''

        try:
            album_name = meta[0].find('a').text
        except:
            album_name = ''

        try:
            released = meta[1].text
        except:
            released = ''

        try:  # 아티스트 2명 이상인경우 끊어서 리스트에 담는다.
            genres = meta[2].text
            genre = list(genres.split('/'))
        except:
            genre = []

        album = {
            'id': album_id,
            'name': album_name,
            'img': album_img
        }
        try:
            lyric = bs.find('div', class_='lyric')
            lyric = str(lyric)
            lyric = re.sub('<.+?>', '/', lyric, 0, re.I|re.S)[11:-2]
        except:
            lyric = ''

        like_res = requests.get(
            f'https://www.melon.com/commonlike/getSongLike.json?contsIds={int(songId)}',
            headers=header
        ).json()
        like = int(like_res['contsLike'][0]["SUMMCNT"])

        song_dict = {
            'id': songId,
            'name': song_name,
            'img': album['img'],
            'artist': artist,
            'released': released,
            'genre': genre,
            'album': album,
            'lyric': lyric,
            'like': like,
            'type': emotion
        }
        song_lst.append(song_dict)

    return song_lst
    # pprint(song_lst)