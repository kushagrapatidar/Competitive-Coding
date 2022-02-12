from time import time

def make_pairs(arr,arr_sorted):
    lst=[]
    for _ in range(N):
        for _2 in range(N):
            if arr[_]!=arr_sorted[_] and arr[_2]!=arr_sorted[_2] and _!=_2 and arr[_]&arr[_2]!=0 and [_2,_] not in lst:
                    lst.append([_,_2])
    return lst

def rearrange(arr,arr_sorted,lst):
    for idx in lst:
        if arr[idx[0]]==arr_sorted[idx[1]] or arr[idx[1]]==arr_sorted[idx[0]]:
            arr[idx[0]],arr[idx[1]]=arr[idx[1]],arr[idx[0]]
    return arr

a=time()
for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int,input().split())]
    arr_sorted=sorted(arr.copy())
    l=1
    while l!=0:
        lst=make_pairs(arr,arr_sorted)
        l=len(lst)
        arr=rearrange(arr,arr_sorted,lst)
    if arr==arr_sorted:
        print("Yes")
    else:
        print("No")
b=time()
print(b-a)