for _ in range(int(input())):
    N,K,M=map(int,input().split())
    S=input()
    if S=='0':
        print(0)
    else:
        N_W=0
        for i in range(len(S)):
            Si=None
            lst=[int(S[i])]
            for _2 in range(M+1):
                Si=[i*K for i in lst]
                lst=[]
                for i in Si:
                    if i==0:
                        lst.append(i)
                    else:
                        while i>0:
                            lst.append(i%10)
                            i=i//10
            N_W+=len(Si)
        print(N_W)