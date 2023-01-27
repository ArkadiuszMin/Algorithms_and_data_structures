from zad9testy import runtests
from collections import deque
from math import inf

def przygotuj(G, sasiedzi, a, b):
    G2 = [[G[i][j] for j in range(len(G[0]))]for i in range (len(G))]
    sasiedzi2 = [[sasiedzi[i][j] for j in range(len(sasiedzi[i]))] for i in range (len(sasiedzi))]
    n=len(G)
    for i in range(n):
        G2[a][i]=0
        G2[b][i]=0

    G2[a][n-1]=inf
    G2[b][n-1]=inf

    sasiedzi2[a].append(n-1)
    sasiedzi2[b].append(n-1)

    return G2, sasiedzi2


def BFS(G, s, t, siec, przeplyw):
    n=len(siec)
    parent=[None]*(n+1)
    visited = [False]*(n+1)
    visited[s]=True

    queue=deque()
    queue.append(s)

    #print(G)

    while queue:
        v = queue.popleft()
        for x in G[v]:
            #print(x)
            if not visited[x] and siec[v][x]!=0:
                visited[x]=True
                parent[x]=v
                queue.append(x)


    if parent[t]==None:
        return False

    x = t
    minimum = inf

    while parent[x] != None:
        if siec[parent[x]][x] < minimum:
            minimum = siec[parent[x]][x]
        x = parent[x]

    x = t
    while parent[x] != None:
        siec[parent[x]][x] -= minimum
        siec[x][parent[x]] += minimum
        przeplyw[parent[x]][x] += minimum
        x=parent[x]

    return True


def highway( G,s ):
    n = 0
    for x in G:
        n = max(n, x[0], x[1])
    n+=1

    Graf = [[0]*(n+1)for j in range(n+1)] #tutaj tez
    sasiedzi = [[] for i in range(n+1)] #tu poszlo +1

    for x in G:
        Graf[x[0]][x[1]]=x[2]
        sasiedzi[x[0]].append(x[1])
        sasiedzi[x[1]].append(x[0])

    maksymalny=0

    for i in range(n):
        if i!=s:
            for j in range(i, n):
                if j!=s and i!=j:
                    przeplyw = [[0]*(n + 1) for i in range(n+1)]
                    x, y = przygotuj(Graf, sasiedzi, i, j)
                    while BFS(y, s, n, x, przeplyw):
                        pass
                    if maksymalny < przeplyw[i][n] + przeplyw[j][n]:
                        maksymalny = przeplyw[i][n] + przeplyw[j][n]

    return maksymalny



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )