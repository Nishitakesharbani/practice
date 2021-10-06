things=['a','b','c','d']
print(things[1])
things[1]="z"
print(things[1])
print(things)


suff={'name': 'Zed', 'age':'39','height':6*12+2}
print(suff['name'])
print(suff['age'])
print(suff['height'])
suff['city']="SF"
print(suff)

suff[1]="wow"
suff[2]="Neato"
print(suff)

suff.pop('city')
suff.pop(1)
suff.pop(2)
print(suff)