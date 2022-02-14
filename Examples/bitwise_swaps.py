for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int,input().split())]
    swaps=0
    i=0
    while i<N:
        j=N-1
        while j>1:
            if (arr[i]&arr[j]==0) or (arr[i]&arr[j]!=0 and arr[i]<arr[j]):
                i+=1
            elif arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                swaps+=1
                i+=1
                j-=1
    if swaps==0:
        print("No")
    else:
        print("Yes")