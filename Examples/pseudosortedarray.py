for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            count+=1
        if i<n-2 and arr[i]>arr[i+2]:
            count+=1
        if count>1:
            print("NO")
            break
    if count<=1: print("YES")