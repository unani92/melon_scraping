import json # import json module
from pprint import pprint
from konlpy.tag import Okt
import re

# 가사들 전처리해야됨......

with open('summer.json') as summer_file:
    summer_data = json.load(summer_file)

with open('sad.json') as sad_file:
    sad_data = json.load(sad_file)

pprint(sad_data[0:3])
# text = re.sub('/', ' ', readData)  # 슬래시 제거



