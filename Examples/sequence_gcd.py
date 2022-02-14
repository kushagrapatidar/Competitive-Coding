from math import gcd
def find_gcd(A):
    GCD=0
    for i in A:
        GCD=gcd(GCD,i)
    return GCD

for _ in range(int(input())):
    N,M=map(int,input().split())
    A=[x for x in map(int,input().split())]
    GCD=[]
    if M==0 or M==1:
        print(find_gcd(A))
    else:
        for i in range(1,M+1):
            lst=[x%i for x in A]
            if sum(lst)==M:
                B=[A[i]-lst[i] for i in range(len(A))]
                GCD.append(find_gcd(B))
        print(max(GCD))
    