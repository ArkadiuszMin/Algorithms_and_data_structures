# ARKADIUSZ MINCBERGER
# Program jest zmodyfikowanym bucket sortem.Na poczatku oblicza on prawdopodobienstwo wystapienia kazdej z cyfr w tablicy T, dzielac
# prawdopodobienstwo przedzialu w ktorym sie ona znajduje przez ilosc liczb w tym przedziale (naturalnych), a nastepnie wyznacza
# dystrybuante, na ktorej opiera sie caly bucket. Nastepnie wylicza przedzial jednego bucketa (7*(1/n), stala 7 na poczatku zostala
# wyznaczona doswiadczalnie) i robi n//7 bucketow. Nastepnie patrzy ile przedzialow bucketa zmiesci sie w "dystrybuancie" danej liczby i
# wrzuca ja do bucketa z indeksem rownym poprzedniej operacji. Potem chodzi po wszystkich bucketach i jesli trzeba to jest sortuje a potem wylewa ich zawartosc
# do tablicy T.
# Zlozonosc: zakladajac ze p=len(P) < n=len(T), przejscie po tablicy P trwa O(len(p)), wyznaczenie dystrybuanty rowniez O(p), przejscie po tablicy T O(n) i przejrzenie
# bucketow O(n//7). Z racji ze n jest najwieksza z tych liczb caly algorytm ma zlozonosc O(n)



from zad3testy import runtests

def insertion(tab, n):
    if n==2:
        if tab[0]>tab[1]:
            tab[0], tab[1] = tab[1], tab[0]
    else:
        for i in range(1, n):
            for j in range(i, 0, -1):
                if tab[j]<tab[j-1]:
                    tab[j], tab[j-1] = tab[j-1], tab[j]
                else:
                    break
def SortTab(T,P):
    p=len(P)
    n=len(T)
    w=0
    B = [0 for _ in range(n+1)]
    for i in range(p):
        a, b, c = P[i]
        if c > 0:
            B[a-1]+=c/(b-a+1)
            B[b]-=c/(b-a+1)
    for i in range(1, n+1):
        B[i]+=B[i-1]
    for i in range(1, n+1):
        B[i] += B[i-1]
    buckets = [[] for _ in range ((n//7)+1)]
    for i in range(n):
        buckets[int((B[int(T[i]-1)] + (B[int(T[i])] - B[int(T[i]-1)])*(T[i]%1))*((n//7)+1))].append(T[i])
    for i in range((n//7)+1):
        k=len(buckets[i])
        if k>1:
            insertion(buckets[i], k)
        if k:
            for j in range(k):
                T[w]=buckets[i][j]
                w+=1
    return T









runtests( SortTab )