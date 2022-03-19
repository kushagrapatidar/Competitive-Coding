for _ in range(int(input())):
    N=int(input())
    S=input()
    xor=0
    for i in range(1,N+1):
        for j in range(N):
            if j+i>=N:
                xor^=int(S[j:N],2)
                break
            else:
                xor^=int(S[j:j+i],2)
    print(xor%998244353)