n=int(input(''))
preflst=[]
pref=dict()
for i in range(n):
    pref['likes']=input('').split()
    pref['dislikes']=input('').split()
    preflst.append(pref.copy())

all_likes=[]
all_dislikes=[]

for pr in preflst:
    if pr['likes'][0]!='0':
        x=int(pr['likes'][0])+1
        for like in pr['likes'][1:x]:
            if like not in all_likes:
                all_likes.append(like)
    
    if pr['dislikes'][0]!='0':
        x=int(pr['dislikes'][0])+1
        for dislike in pr['dislikes'][1:x]:
            if dislike not in all_dislikes:
                all_dislikes.append(dislike)

for dislike in all_dislikes:
    if dislike in all_likes:
        all_likes.remove(dislike)
        
onepizza=all_likes
print(len(onepizza),end=' ')
for ingredient in onepizza:
    print(ingredient,end=' ')