def printing(A,B,C):
    if A+B+C==N and A>=0 and B>=0 and C>=0:
        print("Yes")
        print(A,B,C)
    else:
        print("No")

for _ in range(int(input())):
    N,X=map(int,input().split())
    A=0
    B=0
    C=0
    if X<0 or X>3*N:
        print("No")
    elif X==3*N:
        A=N
        printing(A,B,C)
    elif X==0:
        C=N
        printing(A,B,C)
    elif 0<X<3*N:
        if X%3==0:
            A=X//3
            C=N-A
        elif X%3==1:
            A=X//3+1
            B=2
            C=N-A-B
        elif X%3==2:
            A=X//3+1
            B=1
            C=N-A-B
        printing(A,B,C)
    else:
        print("No")