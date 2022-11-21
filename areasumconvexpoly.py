for _ in range(int(input())):
    N=int(input())
    vertice_lst=[]
    for _2 in range(N):
        vertice_lst.append(list(map(int, input().split())))
    vertice_lst.append(vertice_lst[0])
    for i in range(N):
        for j in range(i+1,N-1):
            ((vertice_lst[j][0]*vertice_lst[j+1][1])-(vertice_lst[j][1]*vertice_lst[j+1][0]))//2