for _ in range(int(input())):
    N=int(input())
    tree=list(map(int,input().split()))
    edges=[]
    for _2 in range(N-1):
        X,Y=map(int,input().split())
        edges.append(list(X,Y))