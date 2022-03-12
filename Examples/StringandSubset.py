from itertools import combinations
for _ in range(int(input())):
    N=int(input())
    S=list(input())
    l=len(S)
    lst=[]
    for i in range(N+1):
        lst+=list(combinations(S,i))
    l2=len(lst)
    lst2=[]
    for _2 in lst:
        s=""
        l1=s.join(_2)
        lst2.append(s)
    lst=lst2
    print(lst)