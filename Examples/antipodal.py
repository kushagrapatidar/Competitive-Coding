from itertools import combinations

for _ in range(int(input())):
    n=int(input())
    p=[None]*n
    for i in range(n):
        p[i]=list(map(int,input().split()))
    idxs=[i for i in range(n)]
    ts=list(combinations(idxs,3))
    hts=0
    for t in ts:
        d=[]
        pts=list(combinations(t,2))
        for pt in pts:
            a,b=pt
            d.append(((p[a][0]-p[b][0])**2 + (p[a][1]-p[b][1])**2)**(0.5))
        e=0.01
        if d[0]+d[1]==d[2] or d[1]+d[2]==d[0] or d[0]+d[2]==d[1]:
            continue
        elif (abs(d[0]**2+d[1]**2-d[2]**2)<e or abs(d[1]**2+d[2]**2-d[0]**2)<e) or abs(d[0]**2+d[2]**2-d[1]**2)<e:
            hts+=1
    print(hts)
