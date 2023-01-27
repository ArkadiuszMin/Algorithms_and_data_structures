# ARKADIUSZ MINCBERGER
# Zaproponowany algorytm przechodzi graf DFSem z taka poprawka ze sprawdza ktora brama wjechal do danego miasta i sprawdza tylko sasiadow z drugiej
# bramy. Jezeli w pewnym momencie zmienna time bedzie rowna ilosci wierzcholkow, co jest rownoznaczne z przejsciem wszystkich miast, a sasiadem ostatniego miasta bedzie
# miasto poczatkowe to znaczy ze szukany cykl istnieje i mozna zakonczyc prace programu. MagicJohnson przechowuje ostatnie miasto w cyklu a dzieki tablicy parent
# program jest w stanie odtworzyc cykl.
# Zlozonosc pamieciowa wynosi O(n) gdzie n to rozmiar tablicy G, a obliczeniowa O(2^n*V) gdyz sprawdzam kazda konfiguracje wierzcholkow (no prawie kazda) i sprawdzam
# sasiadow kazdego wierzcholka w celu ogarniecia bramy


from zad7testy import runtests

def DFS( G ):

    def DFSvisit(G, v, brama):
        nonlocal MagicJohnson
        nonlocal time
        nonlocal n
        #print(time)

        time+=1
        visited[v] = True

        for x in (G[v][brama]):

            if x == 0 and time == n:
                MagicJohnson = v
                return True

            if visited[x]!=True:

                parent[x]=v

                if v in G[x][0]:
                    if DFSvisit(G, x, 1):
                        return True
                else:
                    if DFSvisit(G, x, 0):
                        return True

                parent[x]=None
        time-=1
        visited[v]=False
        return False

    MagicJohnson = None
    n = len(G)
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    parent[0] = 0
    time = 0

    visited[0]=True

    if not DFSvisit(G, 0, 0):
        return None


    sciezka = []

    while MagicJohnson != 0:
        sciezka.append(MagicJohnson)
        MagicJohnson=parent[MagicJohnson]

    sciezka.append(0)

    return sciezka



def droga( G ):
    droga = DFS(G)





    return droga

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )