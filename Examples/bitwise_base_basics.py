T  = int(input())

inputs = []
for ind in range(T):
    
    N, K = map(int, input().split())
    
    binary_string = input()
    inputs.append([N, K, binary_string])

for in_put in inputs:
    K = in_put[1]
    mid = len(in_put[2])//2
    string = in_put[2]
    length=len(string)
    oprations = 0
    for i in range(mid+1):
        if string[i]!=string[-i]:
            oprations+=1
    if oprations>K:
        print("NO")

    elif K==oprations:
        print("YES") 
               
    elif (K-oprations)%2==0:
        print("YES")

    else:
        print("NO")    

####################################################################

T  = int(input())

inputs = []
for ind in range(T):
    
    N, K = map(int, input().split())
    
    binary_string = input()
    inputs.append([N, K, binary_string])

print(inputs)
for in_put in inputs:
    K = in_put[1]
    mid = len(in_put[2])//2
    string = in_put[2]
    oprations = 0
    i=0

    while i+1<=mid:
        if string[i] != string[-(i+1)]:
            oprations += 1 
        i+=1    

    if oprations>K:
        print("NO")

    elif K==oprations:
        print("YES") 
               
    elif (K-oprations)%2==0:
        print("YES")

    else:
        print("NO") 