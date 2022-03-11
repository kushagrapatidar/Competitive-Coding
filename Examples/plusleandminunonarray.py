for _ in range(int(input())):
    N=int(input())
    A=list(map(int,input().split()))
    l=len(A)
    for i in range(l):
        if A[i]<0:
            A[i]=A[i]*(-1)
    A1=[]
    A2=[]
    for i in range(l):
        if i%2==0:
            A1.append(A[i])
        else:
            A2.append(A[i])
    for
    maximum=max(A2)
    minimum=min(A1)
    min_index=A.index(minimum)
    max_index=A.index(maximum)
    if max_index>=min_index and maximum>minimum:
        A[max_index],A[min_index]=A[min_index],A[max_index]
    elif minimum>maximum:
        A1.remove(minimum)
        
    
    sum=0
    for i in range(l):
        sum=pow(-1,i)*A[i]+sum
    print(sum)