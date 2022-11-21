for _ in range(int(input())):
    A,B=map(int,input().split())
    A=A*10
    B=B*5
    if A>B:
        print("FIRST")
    elif A<B:
        print("SECOND")
    else:
        print("ANY")