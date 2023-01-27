# ARKADIUSZ MINCBERGER
# Program szuka najkrotszej sciezki do s i do t dla kazdego wierzcholka. Nastepnie przechodzi przez wierzcholki najkrotszej sciezki, i sprawdza, czy
# dla nich istnieje jakas inna sciezka prowadzaca z t do s. Jesli tak to zwiekszda licznik. Nastepnie patrzy czy w danym wierzcholku jakies takie drogi
# sie spotykaja. Jesli tak to zmniejsza licznik. Jezeli licznik wynosi 0 a w danym wierzcholku nie ma skrzyzowania to usuniecie tej krawedzi potencjalnie
# moze zwiekszyc sciezke, chyba ze istnieje jakas inna niezalezna. Przechodze wiec jeszcze raz BFSem i sprawdzam czy sciezka zaiste sie zmneijszyla

from zad6testy import runtests

from collections import deque


def BFS(G, s, visited):
     #visited, dlugosc, parent
    queue = deque()
    queue.append(s)
    visited[s]=(True, 0, s)
    while queue:
        i=queue.popleft()
        for x in G[i]:
            if visited[x][0]==False:
                queue.append(x)
                visited[x]=(True, visited[i][1]+1, i)





def longer( G, s, t ):
    n = len(G)

    visited = [(False, 0, 0) for _ in range(n)]
    BFS(G, s, visited)

    visited2 = [(False, 0, 0) for _ in range(n)]
    BFS(G, t, visited2)

    sciezka = visited[t][1]
    rozstep=0
    if sciezka==0:
        return None
    k = t
    l = k

    flagunia=True

    while visited[k][1]!=0:
        flagunia=False
        droga = visited[k][1]
        parent = visited[k][2]

        for x in G[k]:
            if visited[x][1]==droga-1 and x!=parent:
                flagunia=True
                rozstep+=1

        for x in G[k]:
            if visited[x][1]==droga+1 and x!=l and visited2[x][1]==sciezka-droga-1:
                rozstep-=1

        if flagunia==False and rozstep <=0:
            for i in range(len(G[k])):
                if G[k][i]==parent:
                    G[k][i]=k

            for i in range(len(G[parent])):
                if G[parent][i]==k:
                    G[parent][i]=parent

            visited = [(False, 0, 0) for _ in range(n)]
            BFS(G, s, visited)

            if visited[t][1]==sciezka:
                return None
            return (parent, k)
        l=k
        k=parent
    return None






# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )