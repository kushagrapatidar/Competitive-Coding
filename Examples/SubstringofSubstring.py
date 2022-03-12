for _ in range(int(input())):
    S=list(input())
    l=len(S)-1
    P=[]
    i=0
    for j in range(l+1):
        lst=[]
        while i<=l:
            if S[i]!=S[0] and S[i]!=S[l]:
                lst.append(S[i])
                i+=1
            else:
                i+=1
                break
        P.append(len(lst))
    maximum=max(P)
    if maximum==0:
        print(-1)
    else:
        print(maximum)