def DFS(G):

    def DFSvisit(G, s, cykl):

        for i in range (len(G[s])):
            if G[s][i] == None:
                continue

            p=G[s][i]

            for j in range(len(G[p])):
                if G[p][j] == s:
                    G[p][j] = None
                    break

            G[s][i] = None
            DFSvisit(G, p, cykl)

        cykl.append(s)

    cykl = []

    for i in G:
        if len(i)%2 != 0:
            return False

    DFSvisit(G, 0, cykl)

    return cykl



G = [
    [2, 1, 4, 3], #0
    [0, 4, 3, 2], #1
    [0, 1, 4, 3], #2
    [2, 1, 4, 0, 5, 6], #3
    [0, 1, 2, 3], #4
    [3, 6], #5
    [5, 3], #6
]
#wynik : [0, 3, 6, 5, 3, 4, 2, 3, 1, 4, 0, 1, 2, 0]

print(DFS(G))










