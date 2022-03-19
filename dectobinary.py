n=int(input())
binary=""
while n>0:
    if n%2==1:
        binary="1"+binary
    else:
        binary="0"+binary
    n//=2
print(binary)