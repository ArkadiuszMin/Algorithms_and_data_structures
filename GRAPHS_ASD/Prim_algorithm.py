from queue import PriorityQueue
#PQ.put - dodaje do kolejki
#PQ.get - bierze
#koeljka typu min



def Prim(G, s):
    n = len(G)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    waga = [2**10 for i in range(n)]
    waga[s] = 0
    PQ = PriorityQueue()
    PQ.put((waga[s], s))
    while not PQ.empty():
        _, a = PQ.get()
        if visited[a]:
            continue
        visited[a]=True
        for x, y in G[a]:
            if waga[x]>y and parent[a]!=x:
                parent[x]=a
                waga[x]=y
                PQ.put((waga[x], x))
    return parent


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



print(Prim(G, 0))
