from math import gcd
def find_gcd(A):
    GCD=0
    for i in A:
        GCD=gcd(GCD,i)
    return GCD

for _ in range(int(input())):
    N,M=map(int,input().split())
    A=[x for x in map(int,input().split())]
    print(find_gcd(A))