from zad11ktesty import runtests

def rekurencja(T, F, s1, s2, indeks):

    if indeks < 0:
        return abs(s1 - s2)

    if F[indeks][s1] != -1:
        return F[indeks][s1]

    F[indeks][s1] = min(rekurencja(T, F, s1 + T[indeks], s2, indeks-1), rekurencja(T, F, s1, s2+T[indeks], indeks-1))
    return F[indeks][s1]



def kontenerowiec(T):
    n = len(T)

    #Tutaj proszę wpisać własną implementację
    suma = 0
    for i in range(n):
        suma+=T[i]
    F = [[-1 for i in range(suma+1)]for j in range(n)]
    return rekurencja(T, F, 0, 0, n-1)

runtests ( kontenerowiec )
    