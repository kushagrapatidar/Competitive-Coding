for _ in range(int(input())):
    N,X=map(int,input().split())
    A=list(map(int,input().split()))
    n=0
    for i in range(len(A)):
        if A[-(i+1)]<X:
            n=N-i
            break
    print(n)