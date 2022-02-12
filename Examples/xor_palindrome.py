for _ in range(int(input())):
    N=int(input())
    S=input()
    counts=[0,0]
    if N==0:
        print("No")
    else:
        for i in range(N):
            
            if S[i]=='0':
                counts[0]+=1
    
            elif S[i]=='1':
                counts[1]+=1
        
        if N%2==0:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==0 and (counts[0]%2 or counts[1]%2)==0:
                print("Yes")
            else:
                print("No")
        else:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==1:
                print("Yes")
            else:
                print("No")