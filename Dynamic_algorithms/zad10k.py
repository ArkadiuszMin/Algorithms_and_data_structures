from zad10ktesty import runtests
from math import inf
def dywany ( N ):

    F = [inf for i in range(N+1)]
    ciecie = [-1 for i in range (N+1)]
    F[0]=0
    F[1]=1
    F[2]=2
    F[3]=3
    ciecie[0] = -1
    ciecie[1] = 1
    ciecie[2] = 1
    ciecie[3] = 1

    for i in range(4, N+1):
        j = 1
        while j*j <= i:
            if F[i-j*j] + 1 < F[i]:
                F[i] = F[i-j*j] + 1
                ciecie[i] = j
            j+=1
    wyniki = []
    indeks = N
    while ciecie[indeks] != -1:
        wyniki.append(ciecie[indeks])
        indeks-=ciecie[indeks]*ciecie[indeks]


    return wyniki





runtests( dywany )

