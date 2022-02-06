for _ in range(int(input())):
    N,K,M=map(int,input().split())
    S=input()
    if S=='0':
        print(0)
    else:
        S=[int(power) for power in S]
        for _2 in range(M):
            N_new=len(S)
            S=[S[i]*K for i in range(N_new)]
            N_new=len(S)
            for _3 in range(N_new):
                if S[0]==0:
                    S.append(S[0])
                else:
                    while S[0]>0:
                        S.append(S[0]%10)
                        S[0]=S[0]//10
                S=S[1:]
        print(len(S))