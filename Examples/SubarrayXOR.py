for _ in range(int(input())):
    N=int(input())
    S=input()
    l=len(S)
    lst=[]
    i=1
    while i<=N:
        for j in range(N):
            if j+i>=N:
                lst.append(int(S[j:N],2))
                break
            else:
                lst.append(int(S[j:j+i],2))
        i+=1
    for i in range(1,len(lst)):
        lst[i]=lst[i-1]^lst[i]
    print(lst[-1]%998244353)