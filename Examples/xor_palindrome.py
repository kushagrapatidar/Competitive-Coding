for _ in range(int(input())):
    N=int(input())
    S=input()
    zeros=0
    ones=0
    
    for i in range(N):
        
        if S[i]=='0':
            zeros+=1

        else:
            ones+=1
    
    if N%2==0:
        if (zeros%2==0 and ones%2==0) or zeros==ones:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")