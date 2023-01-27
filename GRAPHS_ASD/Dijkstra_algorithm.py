from queue import PriorityQueue



def Dijkstra(G, s):

    def relax(x, y, wagunia):
        if szacunek[y] > szacunek[x] + wagunia:
            szacunek[y] = szacunek[x] + wagunia
            parent[y]=x
            return True
        return False

    n = len(G)
    visited=[False for i in range(n)]
    parent = [None for i in range(n)]
    szacunek = [2**15 for i in range(n)]
    szacunek[0]=0
    PQ = PriorityQueue()
    PQ.put((szacunek[s], s))
    while not PQ.empty():
        y, x = PQ.get()
        if visited[x]:
            continue
        visited[x]=True
        for i in G[x]:
            if relax(x, i[0], i[1]):
                PQ.put((szacunek[i[0]], i[0]))

    return szacunek

G = [[(1, 2), (2, 4)], [(0, 2), (2, 1), (3, 4)], [(0, 4), (1, 1), (4, 1), (3, 2)], [(1, 4), (2, 2), (5, 1)], [(2, 1), (5, 3)], [(3, 1), (4, 3)]]

print(Dijkstra(G, 0))