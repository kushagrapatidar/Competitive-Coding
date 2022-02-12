for _ in range(int(input())):
    N=int(input())
    S=input()
    xor_count=[0,0]
    ele_lst=[[],[]]
    for i in range(N//2):
        if S[i]^S[N-i-1]==0:
            xor_count[0]+=1
            ele_lst[0]=[S[i],S[N-i-1]]
        elif S[i]^S[N-i-1]==1:
            xor_count[1]+=1
            ele_lst[1]=[S[i],S[N-i-1]]
    xor=max(xor_count[0],xor_count[1])
    print(xor)
    print(xor)