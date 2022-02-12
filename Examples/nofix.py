for _ in range(int(input())):
    N=int(input())
    A=[]
    for x in map(int,input().split()):
        A.append(x)
    x=0
    for i in range(N):
        num=1+i+x
        if num==A[i]:
            x+=1
    print(x)