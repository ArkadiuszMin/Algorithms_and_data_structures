# f(x) - najdluzszy wspolny podciag do i-tego elementu pod warunkiem ze go biore
#f(x) = max f(i)+1, (i = 0,1,...,x-1) jesli T[i] < T[x]


def podciag(T):
    n = len(T)
    F = [0 for i in range (n)]
    parent = [None for i in range(n)]
    F[0] = 1
    for i in range(1, n):
        for j in range(i):
            if T[j]<T[i] and F[j]+1>F[i]:
                parent[i]=j
                F[i]=F[j]+1
    maks = 0
    for i in range(n):
        if F[i]>maks:
            maks = F[i]
            indeks = i
    wynik = []

    while indeks is not None:
        wynik.append(T[indeks])
        indeks=parent[indeks]

    print(wynik)

T =[2, 1, 4, 3, 4, 8, 5, 7, 2, 0]
podciag(T)
