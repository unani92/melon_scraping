from bs4 import BeautifulSoup
import requests
from scrap import scrap

import json

header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Trident/7.0;rv:11.0) like Gecko"}

# # 슬픈노래
# sad1_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=402475544', headers=header).text
# sad1_bs = BeautifulSoup(sad1_html, "html.parser")
# sad_1 = sad1_bs.select('tr')[1:]
#
# sad2_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=481799191', headers=header).text
# sad2_bs = BeautifulSoup(sad2_html, "html.parser")
# sad_2 = sad2_bs.select('tr')[1:]
#
# sad3_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=481799191', headers=header).text
# sad3_bs = BeautifulSoup(sad3_html, "html.parser")
# sad_3 = sad3_bs.select('tr')[1:]
#
# sad4_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=440463657', headers=header).text
# sad4_bs = BeautifulSoup(sad4_html, "html.parser")
# sad_4 = sad4_bs.select('tr')[1:]
#
# sad5_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=415794503', headers=header).text
# sad5_bs = BeautifulSoup(sad5_html, "html.parser")
# sad_5 = sad5_bs.select('tr')[1:]
#
# sad6_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=446613076', headers=header).text
# sad6_bs = BeautifulSoup(sad6_html, "html.parser")
# sad_6 = sad6_bs.select('tr')[1:]
#
# sad7_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=423777277', headers=header).text
# sad7_bs = BeautifulSoup(sad7_html, "html.parser")
# sad_7 = sad7_bs.select('tr')[1:]
#
# sad8_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=438210125', headers=header).text
# sad8_bs = BeautifulSoup(sad8_html, "html.parser")
# sad_8 = sad8_bs.select('tr')[1:]
#
# sad = scrap(sad_1,'sad') + scrap(sad_2, 'sad') + scrap(sad_3, 'sad')\
#       + scrap(sad_4, 'sad') + scrap(sad_5, 'sad') + scrap(sad_6, 'sad')\
#       + scrap(sad_7, 'sad') + scrap(sad_8, 'sad')
#
# sad_file = open("sad.json", "w+")
# sad_file.write(json.dumps(sad))
# print('sad finish')
#
# # 신나는 노래
# summer1_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=432011657', headers=header).text
# summer1_bs = BeautifulSoup(summer1_html, "html.parser")
# summer_1 = summer1_bs.select('tr')[1:]
#
# summer2_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=421161632', headers=header).text
# summer2_bs = BeautifulSoup(summer2_html, "html.parser")
# summer_2 = summer2_bs.select('tr')[1:]
#
# summer3_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=421161632#params%5BplylstSeq%5D=421161632&po=pageObj&startIndex=51', headers=header).text
# summer3_bs = BeautifulSoup(summer3_html, "html.parser")
# summer_3 = summer3_bs.select('tr')[1:]
#
# summer4_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=433139568', headers=header).text
# summer4_bs = BeautifulSoup(summer4_html, "html.parser")
# summer_4 = summer4_bs.select('tr')[1:]
#
# summer5_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=427175003', headers=header).text
# summer5_bs = BeautifulSoup(summer5_html, "html.parser")
# summer_5 = summer5_bs.select('tr')[1:]
#
# summer6_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=430702430', headers=header).text
# summer6_bs = BeautifulSoup(summer6_html, "html.parser")
# summer_6 = summer6_bs.select('tr')[1:]
#
# summer7_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=425660073', headers=header).text
# summer7_bs = BeautifulSoup(summer7_html, "html.parser")
# summer_7 = summer7_bs.select('tr')[1:]
#
# summer = scrap(summer_1, 'joy') + scrap(summer_2, 'joy') + scrap(summer_3, 'joy') + scrap(summer_4, 'joy') + scrap(summer_5, 'joy') + scrap(summer_6, 'joy') + scrap(summer_7, 'joy')
#
# summer_file = open("summer.json", "w+")
# summer_file.write(json.dumps(summer))
# print('summer finish')
#
#
# # 새벽감성
# midnight1_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=425660073', headers=header).text
# midnight1_bs = BeautifulSoup(midnight1_html, "html.parser")
# midnight_1 = midnight1_bs.select('tr')[1:]
#
# midnight2_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=437818111', headers=header).text
# midnight2_bs = BeautifulSoup(midnight2_html, "html.parser")
# midnight_2 = midnight2_bs.select('tr')[1:]
#
# midnight3_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=434678849', headers=header).text
# midnight3_bs = BeautifulSoup(midnight3_html, "html.parser")
# midnight_3 = midnight3_bs.select('tr')[1:]
#
# midnight4_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=415828654', headers=header).text
# midnight4_bs = BeautifulSoup(midnight4_html, "html.parser")
# midnight_4 = midnight4_bs.select('tr')[1:]
#
# midnight5_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=477963974', headers=header).text
# midnight5_bs = BeautifulSoup(midnight5_html, "html.parser")
# midnight_5 = midnight5_bs.select('tr')[1:]
#
# midnight6_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=431708895', headers=header).text
# midnight6_bs = BeautifulSoup(midnight6_html, "html.parser")
# midnight_6 = midnight6_bs.select('tr')[1:]
#
# midnight = scrap(midnight_1, 'midnight') + scrap(midnight_2, 'midnight') + scrap(midnight_3, 'midnight') + scrap(midnight_4, 'midnight') + scrap(midnight_5, 'midnight') + scrap(midnight_6, 'midnight')
#
# midnight_file = open("midnight.json", "w+")
# midnight_file.write(json.dumps(midnight))
# print('midnight finish')


# 사랑노래
love1_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=482499717', headers=header).text
love1_bs = BeautifulSoup(love1_html, "html.parser")
love_1 = love1_bs.select('tr')[1:]

love2_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=456614879', headers=header).text
love2_bs = BeautifulSoup(love2_html, "html.parser")
love_2 = love2_bs.select('tr')[1:]

love3_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=455444089', headers=header).text
love3_bs = BeautifulSoup(love3_html, "html.parser")
love_3 = love3_bs.select('tr')[1:]

love4_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=430108988', headers=header).text
love4_bs = BeautifulSoup(love4_html, "html.parser")
love_4 = love4_bs.select('tr')[1:]

love5_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=451198655', headers=header).text
love5_bs = BeautifulSoup(love5_html, "html.parser")
love_5 = love5_bs.select('tr')[1:]

love6_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=455324377', headers=header).text
love6_bs = BeautifulSoup(love6_html, "html.parser")
love_6 = love6_bs.select('tr')[1:]

love7_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=455324377', headers=header).text
love7_bs = BeautifulSoup(love7_html, "html.parser")
love_7 = love7_bs.select('tr')[1:]

love8_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=430470805', headers=header).text
love8_bs = BeautifulSoup(love8_html, "html.parser")
love_8 = love8_bs.select('tr')[1:]

love9_html = requests.get('https://www.melon.com/mymusic/dj/mymusicdjplaylistview_inform.htm?plylstSeq=456337994', headers=header).text
love9_bs = BeautifulSoup(love9_html, "html.parser")
love_9 = love9_bs.select('tr')[1:]

love = scrap(love_1, 'love') + scrap(love_2, 'love') + scrap(love_3, 'love')\
       + scrap(love_4, 'love') + scrap(love_5, 'love') + scrap(love_6, 'love')\
       + scrap(love_7, 'love') + scrap(love_8, 'love') + scrap(love_9, 'love')

love_file = open("love.json", "w+")
love_file.write(json.dumps(love))
print('love finish')