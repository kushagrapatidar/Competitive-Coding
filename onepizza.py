n=int(input(''))
preflst=list()
pref=dict()
for i in range(n):
    pref['likes']=input('').split()
    pref['dislikes']=input('').split()
    preflst.append(pref)