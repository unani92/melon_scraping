from bs4 import BeautifulSoup
import requests
import re

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}

def scrap_song(bs_object, header=None):
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
            artist.append(id)

        meta = section_info.select('.list dd')

        try:
            album_id = meta[0].find('a')['href']
            album_id = int(re.findall("\d+", album_id)[0])
        except:
            album_id = ''

        try:
            released = meta[1].text
        except:
            released = ''

        try:  # 아티스트 2명 이상인경우 끊어서 리스트에 담는다.
            genres = meta[2].text
            genre = list(genres.split(', '))
        except:
            genre = []

        album = album_id
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
            'model': 'music.song',
            'pk': songId,
            'fields': {
                'name': song_name,
                'img': album_img,
                'artist': artist,
                'released': released,
                'genres': genre,
                'album': album,
                'lyric': lyric,
                'like': like,
                'type': ''
            }
        }

        song_lst.append(song_dict)

    return song_lst

def scrap_artist(artists, header=None):
    if header is None:
        header = headers

    artist_lst = []
    for idx, artist in enumerate(artists):
        try:
            artist_html = requests.get(f'https://www.melon.com/artist/detail.htm?artistId={artist}', headers=header).text
            artist_bs = BeautifulSoup(artist_html, "html.parser")
            artist_div = artist_bs.find('div', class_='dtl_atist clfix')

            # artist id
            artist_id = artist
            # artist img, name
            try:
                img = artist_div.find(id='artistImgArea').find('img')['src']
            except:
                img = ''
            try:
                artist_name = artist_div.find('p', class_='title_atist').text[5:]
                artist_name = artist_name.split('\xa0')[0]
                artist_name = re.sub(r'\([^)]*\)', '', artist_name)
                if artist_name[-1] == '':
                    artist_name = artist_name[-1]
            except:
                artist_name = ''
            # artist_debue
            artist_info_dd = artist_div.find('dl', class_='atist_info clfix').select('dd')
            artist_info_dt = artist_div.find('dl', class_='atist_info clfix').select('dt')

            artist_info = dict()
            for i in range(len(artist_info_dd)):
                artist_info[artist_info_dt[i].text] = artist_info_dd[i].text

            try:
                artist_debue = artist_info['데뷔']
                artist_debue = artist_debue.split('\n')[1]

                # artist_debue = re.findall("\d+",artist_debue)
                # artist_debue = ''.join(artist_debue)
            except:
                artist_debue = ''
                # artist_type
            try:
                artist_type = artist_info['활동유형']
            except:
                artist_type = '솔로'
            if artist_type == '그룹':
                members_div = artist_div.find('div', class_='wrap_atistname')
                members_a = members_div.select('a')
                members = ''
                for member in members_a:
                    members += member['title'] + ' '
                members = members[:-1]
            else:
                members = ''

            artist_dic = {
                'model': 'music.artist',
                'pk': artist_id,
                'fields': {
                    'name': artist_name,
                    'img': img,
                    'debue': artist_debue,
                    'type': artist_type,
                    'member': members
                }
            }

            artist_lst.append(artist_dic)

        except:
            print(f'아티스트 {idx-1}/{len(artists)}까지 돌아가다 멈춤!!!')
            return artist_lst

    return artist_lst

def scrap_album(albums, header=None):
    if header == None:
        header = headers

    album_lst = []
    for idx, album in enumerate(albums):
        try:
            album_html = requests.get(f'https://www.melon.com/album/detail.htm?albumId={album}', headers=header).text
            album_bs = BeautifulSoup(album_html, "html.parser")

            album_div = album_bs.find('div', class_='wrap_info')

            # img
            img = album_div.find('img')['src']

            entry = album_div.find('div', class_='entry')

            # name
            name = entry.find('div', class_='song_name').text
            name = re.sub(r"\s+", " ", name)[5:-1]

            # artist
            try:
                artist = entry.find('div', class_='artist').find('a')['href']
                artist = int(re.findall('\d+', artist)[0])
            except:
                artist = 1

            dl = entry.find('dl', class_='list')
            album_info_dd = dl.select('dd')
            album_info_dt = dl.select('dt')

            album_info = dict()
            for i in range(len(album_info_dd)):
                album_info[album_info_dt[i].text] = album_info_dd[i].text

            # released_date
            released_date = album_info['발매일']
            released_date = ''.join(re.findall('\d+', released_date))

            # genre
            genres = album_info['장르'].split(', ')

            # like
            like_res = requests.get(
                f'https://www.melon.com/commonlike/getAlbumLike.json?contsIds={int(album)}',
                headers=header
            ).json()
            like = int(like_res['contsLike'][0]["SUMMCNT"])

            album_dic = {
                'model': 'music.album',
                'pk': album,
                'fields': {
                    'img': img,
                    'name': name,
                    'artist': artist,
                    'released_date': released_date,
                    'genres': genres,
                    'like': like
                }
            }
            album_lst.append(album_dic)
        except:
            print(f'앨범 {idx-1}/{len(albums)}까지 하다 멈춤')
            return

    return album_lst