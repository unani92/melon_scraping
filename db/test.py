# L=[
#     {'id':1,'name':'john', 'age':34},
#     {'id':1,'name':'john', 'age':34},
#     {'id':2,'name':'hanna', 'age':30},
# ]
#
# a = list({v['id']:v for v in L}.values())
# print(a)

a = [1,1,1,1,1,2,3,4]

print(list(set(a)))