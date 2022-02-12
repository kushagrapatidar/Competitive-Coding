#Bubble Sort

for _ in range(int(input())):
    N=int(input())
    arr=map(int,input().spit())
    arr_sorted=arr.copy().sort()
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            num=arr[i]
            next_num=arr[i+1]
            if num>next_num and num&next_num!=0:
                arr[i],arr[i+1]=next_num,num
    if arr==arr_sorted:
        print("Yes")
    else:
        print("No")