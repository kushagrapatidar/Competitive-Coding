for _ in range(int(input())):
    N=int(input())
    if N<2: print(N)
    elif N%2==0: print(N//2)
    else: print(N//2+1)