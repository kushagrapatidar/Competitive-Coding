for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int,input().split())]
    lst=[]
    for _ in range(N):
        for _2 in range(N):
            if _!=_2 and arr[_]&arr[_2]!=0 and [_2,_] not in lst:
                lst.append([_,_2]) 
    print(lst) 