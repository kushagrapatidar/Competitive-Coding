from math import factorial

def sumofdigits(n):
    sumofdigit=0
    while n>0:
        sumofdigit+=n%10
        n//=10
    return sumofdigit

def sumoffact(n):
    sumfactorial=0
    while n>0:
        sumfactorial+=factorial(n%10)
        n//=10
    return sumfactorial

for _ in range(int(input())):
    n,m=map(int, input().split())
    sumofg=0
    for i in range(1,n+1):
        s=None
        j=1
        while True:
            if sumofdigits(sumoffact(j))==i:
                s=j
                break
            j+=1
        sumofg+=sumofdigits(s)
    print(sumofg%m)