def check_arr(arr):
    for _ in range(len(arr)):
        if arr[_]==_+1:
            return _
    return -1
def count_operations(arr,count):
    K=len(arr)+1
    index=check_arr(arr)
    if index==-1:
        print(count)
        return count
    arr.insert(index,K)
    count+=1
    count_operations(arr,count)

for _ in range(int(input())):
    N=int(input())
    arr=[x for x in map(int, input().split())]
    count_operations(arr,0)