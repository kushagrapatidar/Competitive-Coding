for _ in range(int(input())):
    N=int(input())
    S=input()
    n=0
    i=0
    while i<len(S):
        if i==len(S)-1:
            n+=1
        elif S[i]==S[i+1]:
            i+=1
            n+=1
        else:
            n+=1
        i+=1
    print(n)