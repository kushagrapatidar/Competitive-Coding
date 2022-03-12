for _ in range(int(input())):
    S=input()
    T=input()
    M=""
    for i in range(len(T)):
        if T[i]==S[i]:
            M+="G"
        else:
            M+="B"
    print(M)