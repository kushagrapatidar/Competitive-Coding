for _ in range(int(input())):
    n=int(input())
    arr=input().split()
    count=[0,0]
    for i in range(n):
        if arr[i]=='-1':
            count[0]+=1
    count[1]=n-count[0]
    
    if (abs(count[0]-count[1])<2) or (abs(count[0]-count[1])==2 and count[1]%2==0 and count[0]%2==0):
        print("YES")
    else:
        print("NO")