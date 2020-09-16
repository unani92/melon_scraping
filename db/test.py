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

a = scrap_album([342967])
pprint(a)
