for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int,input().split())]
    swaps=0
    for i in range(N):
        for k in range(N):
            j=N-k-1
            if i!=j and arr[i]&arr[j]!=0 and arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                swaps+=1
    if swaps==0:
        print("No")
    else:
        print("Yes")