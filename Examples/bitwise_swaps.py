for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int,input().split())]
    arr_sorted=sorted(arr.copy())
    if arr==arr_sorted:
        print("No")
    else:
        for i in range(N):
            j=N-1
            while j>i:
                if arr[i]&arr[j]!=0 and arr[i]>arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
                    j-=1
                j-=1
        if arr!=arr_sorted:
            print("No")
        else:
            print("Yes")