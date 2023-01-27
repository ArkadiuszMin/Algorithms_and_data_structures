from math import inf

def Floryda(G):
    n = len(G)
    D = [[inf for i in range(n)] for j in range(n)]
    parent = [[None for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            if i==j:
                D[i][j]=0
            if G[i][j]!=0:#ewentualnie inf
                D[i][j]=G[i][j]
                parent[i][j]=i


    for i in range(n):
        for j in range(n):
            for k in range(n):
                if D[j][k] > D[j][i] + D[i][k]:
                    parent[j][k] = i
                    D[j][k] = D[j][i] + D[i][k]
    return D

graph = [[0, 0, 0, 0, -1, 0],
         [1, 0, 0, 2, 0, 0],
         [0, 2, 0, 0, 0, 10],
         [-4, 0, 0, 0, 3, 0],
         [0, 7, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0]]
print(Floryda(graph))


