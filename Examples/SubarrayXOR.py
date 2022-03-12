for _ in range(int(input())):
    N=int(input())
    S=list(input())
    l=len(S)
    lst=[]
    i=1
    while i<=N:
        for j in range(N):
            if j+i>=N:
                lst.append(S[j:N])
                break
            else:
                lst.append(S[j:j+i])
        i+=1
    len_lst=len(lst)
    for i in range(len_lst):
        lst2=""
        lst[i]=int(lst2.join(lst[i]),2)
    xor=None
    for i in range(1,len_lst):
        lst[i]=lst[i-1]^lst[i]
    print(lst[-1])