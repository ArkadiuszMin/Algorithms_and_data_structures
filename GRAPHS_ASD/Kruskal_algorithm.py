#Gdy dana jest lista sasiadow

def edge_list(G):
    edges=[]
    for i in range(len(G)):
        for x in G[i]:
            if i<x[0]:
                edges.append((i, x[0], x[1]))
    return edges


class Node:
    def __init__(self):
        self.parent=None
        self.rank=0

def makeset(x):
    a = Node()
    a.parent=a
    return a

def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x, y):
    a=find(x)
    b=find(y)
    if a==b:
        return False
    if a.rank>b.rank:
        b.parent=a
    else:
        a.parent=b
        if a.rank==b.rank:
            b.rank+=1
    return True


def Kruskal(G):
    A=[]
    n=len(G)
    V=[]
    edges=edge_list(G)
    for i in range(n):
        V.append(makeset(i))
    edges=sorted(edges, key = lambda x: x[2])
    licznik = 0
    for x in edges:
        if union(V[x[0]], V[x[1]]):
            A.append(x)
            licznik+=1
        if licznik==(n-1):
            break
    return A

G=[
    [(2,3),(4,4),(5,33)],
    [(5,2),(6,11),(7,17)],
    [(0,3),(4,33),(6,20),(8,10)],
    [(4,7),(7,18)],
    [(0,4),(2,33),(3,7),(7,28)],
    [(0,33),(1,2),(8,5)],
    [(1,11),(2,20),(8,14)],
    [(1,17),(3,18),(4,28)],
    [(2,10),(5,5),(6,14)]
]

print(Kruskal(G))







