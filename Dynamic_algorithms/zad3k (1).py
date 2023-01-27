from zad3ktesty import runtests
from math import inf
def ksuma( T, k ):
    n = len(T)
    F = [0 for i in range(n)]
    wyniki=[None for i in range(n)]
    for i in range(k):
        F[i] = T[i]
    for i in range(k, n):
        F[i] = T[i]
        minimum=inf
        for j in range(1, k+1):
            if F[i-j]<minimum:
                minimum=F[i-j]
                wyniki[i]=i-j
        F[i]+=minimum

    minimum=inf
    for i in range(k):
        if F[n-1-i]<minimum:
            minimum=F[n-1-i]
            indeks=n-1-i

    tablica=[]
    while indeks is not None:
        tablica.append(T[indeks])
        indeks=wyniki[indeks]
    print(tablica)
    return minimum
    
runtests ( ksuma )