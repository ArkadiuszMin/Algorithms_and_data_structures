from collections import deque
from math import inf


def BFS(G, s, t, siec, przeplyw):
    n=len(G)
    parents=[None for i in range(n)]
    visited = [False for i in range(n)]


    visited[s]=True
    queue = deque()
    queue.append(s)


    while queue:
        v = queue.popleft()
        for x in G[v]:
            if not visited[x] and siec[v][x]!=0:
                parents[x]=v
                visited[x]=True
                queue.append(x)

    if parents[t]==None:
        return False

    #print(parents)

    minimum = inf
    x = t
    while parents[x] != None:
        if siec[parents[x]][x] < minimum:
            minimum = siec[parents[x]][x]
        x=parents[x]


    x=t
    while parents[x] != None:
        siec[parents[x]][x]-=minimum
        siec[x][parents[x]]+=minimum
        przeplyw[parents[x]][x]+=minimum
        x=parents[x]

    return True








def karp(G, s, t):
    n=len(G)
    siec = G
    przeplyw = [[0 for i in range(n)] for j in range(n)]
    sasiedzi = [[] for i in range(n)]


    for i in range(n):
        for j in range(n):
            if G[i][j]!=0:
                sasiedzi[i].append(j)
                if G[i][j]==0:
                    sasiedzi[j].append(i)
    sasiedzi[t]=[]

    while BFS(sasiedzi, s, t, siec, przeplyw):
        pass

    woda=0

    for i in range(n):
        woda+=przeplyw[i][t]

    return woda


graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(karp(graph, 0, 9))



