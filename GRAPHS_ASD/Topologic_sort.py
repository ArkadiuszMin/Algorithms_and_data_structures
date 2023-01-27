def DFS(G):

    def DFSvisit(G, s, binar):
        nonlocal time
        nonlocal pozycja
        nonlocal visited
        visited[s]=True

        for x in G[s]:
            if not visited[x]:
                parent[x] = s
                DFSvisit(G, x, binar)
        binar[pozycja]=s
        pozycja-=1

    n = len(G)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    time = 0
    pozycja = n-1
    binar = [0 for i in range(n)]
    for i in range(n):
        if not visited[i]:
            DFSvisit(G, i, binar)
    return binar


G =[[1,2], [2], [], [], [1,3,6], [4], []]
print(DFS(G))