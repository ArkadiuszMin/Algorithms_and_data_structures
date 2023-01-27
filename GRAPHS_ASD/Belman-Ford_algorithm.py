
from math import inf

def Belmondo(G, s):

    def relax(G, i):
        if szacunek[G[i][1]] > szacunek[G[i][0]] + G[i][2]:
            szacunek[G[i][1]] = szacunek[G[i][0]] + G[i][2]
            parent[G[i][1]]=G[i][0]

    V = 0
    n = len(G)
    for i in range(n):
        V = max(V, G[i][0], G[i][1])
    V+=1
    szacunek=[inf for i in range(V)]
    parent = [None for i in range(V)]
    szacunek[s]=0
    for i in range(V-2):
        for j in range(n):
            relax(G, j)
    for i in range(n):
        if szacunek[G[i][1]] > szacunek[G[i][0]] + G[i][2]:
            return False, parent
    return True, parent

G = [[0, 1, 6], [0, 2, 7], [1, 2, 8], [1, 3, 5], [1, 4, -4], [2, 3, -3],
         [2, 4, 9], [3, 1, -2], [4, 0, 2], [4, 3, 7]]
rezultat, tablica = Belmondo(G, 0)

if not rezultat:
    print("none")

else:
    print(tablica)