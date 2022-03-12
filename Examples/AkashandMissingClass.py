for _ in range(int(input())):
    N=int(input())
    if N<7 and N%7<6:
        print(0)
    elif N%7==6:
        print(N//7+1)
    elif 0<=N%7<6:
        print(N//7)