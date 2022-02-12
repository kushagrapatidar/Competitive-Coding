from tokenize import String


N=[]
Strings=[]
results=[]

for _ in range(int(input())):
    N=int(input())
    Strings.append(input())

for j in range(len(Strings)):
    S=String[j]

    if len(S)!=N[i]:
        results.append("No")
    else:
        counts=[0,0]
        
        for i in range(N[i]):
            
            if S[i]=='0':
                counts[0]+=1
    
            elif S[i]=='1':
                counts[1]+=1
        
        if N[i]%2==0:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==0 and (counts[0]%2 or counts[1]%2)==0:
                results.append("Yes")
            else:
                results.append("No")
        
        else:
            if (max(counts[0],counts[1])-min(counts[0],counts[1]))%2==1:
                results.append("Yes")
            else:
                results.append("No")
for result in results: print(result)