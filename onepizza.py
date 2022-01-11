n=int(input(''))
preflst=[]
pref=dict()
for i in range(n):
    pref['likes']=input('').split()
    pref['dislikes']=input('').split()
    preflst.append(pref.copy())
for pr in preflst:
    print(pr)