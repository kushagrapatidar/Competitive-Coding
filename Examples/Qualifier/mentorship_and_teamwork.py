C,P=map(int,input().split())

#Contributer inputs
contributers=dict()
for _ in range(C):
    contributer,N=input().split()
    N=int(N)
    contributers[contributer]=[]
    for _2 in range(N):
        S,L=input().split()
        L=int(L)
        contributers[contributer].append([S,L])

#Projects Inputs
projects=dict()
project_scoring=[]
for _ in range(P):
    project,D,S,B,R=input().split()
    D,S,B,R=map(int,[D,S,B,R])
    projects[project]=[]
    project_scoring.append([D,S,B])
    for _2 in range(R):
        X,L=input().split()
        L=int(L)
        projects[project].append([X,L])

print(contributers)
print(projects)
    
skills=[]
levels=[]
ckeys=contributers.keys()
for i in range(len(ckeys)):
    cs_l=projects[ckeys[i]]
    cs=[cs_l[j][0] for j in range(len(cs_l))]
    cl=[cs_l[j][1] for j in range(len(cs_l))]
    skills.append(cs)
    levels.append(cl)

pkeys=projects.keys()
for i in range(len(pkeys)):
    ps_l=projects[pkeys[i]]
    ps=[ps_l[j][0] for j in range(len(ps_l))]
    pl=[ps_l[j][1] for j in range(len(ps_l))]
    for rskill in ps:
        pidx=ps.index(rskill)
        for cskills in skills:
            csidx=skills.index(cskills)
            cidx=cskills.index(rskill)
            if rskill in cskills and levels[csidx][cidx]>=pl[pidx]:
                      