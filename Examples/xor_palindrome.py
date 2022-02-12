from tokenize import String


N=0
Strings=[]
results=[]
for _ in range(int(input())):
    N=int(input())
    Strings.append(input())
for S in Strings:
    if len(S)!=N:
        print("No")
    else:
        counts=[0,0]
        for i in range(N):
            
            if S[i]=='0':
                counts[0]+=1
    
            elif S[i]=='1':
                counts[1]+=1
        
        if N%2==0:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==0 and (counts[0]%2 or counts[1]%2)==0:
                results.append("Yes")
            else:
                results.append("No")
        else:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==1:
                results.append("Yes")
            else:
                results.append("No")