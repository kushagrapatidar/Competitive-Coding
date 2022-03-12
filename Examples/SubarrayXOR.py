result=[]
def permute(data, i, length):
    if i == length:
        result.append(''.join(data) )
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i] 
for _ in range(int(input())):
    N=int(input())
    S=input()
    result = []
    permute(list(S),0,N)
    result=list(map(int,result))
    print(result)