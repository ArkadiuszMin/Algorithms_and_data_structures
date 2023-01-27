from zad12ktesty import runtests 
from math import inf

def rek(F, S, k, koniec):
    if koniec==-1:
        return 0

    if F[koniec][k] != -1:
        return F[koniec][k]

    if k == 0:
        F[koniec][k] = S[0][koniec]
        return S[0][koniec]
    if koniec==0:
        F[koniec][k] = S[0][0]
        return S[0][0]
    minimalna=inf
    for j in range(koniec, -1, -1):
        if max(S[j][koniec], rek(F, S, k-1, j-1)) < minimalna:
            minimalna = max(S[j][koniec], rek(F, S, k-1, j-1))
    F[koniec][k]=minimalna
    return minimalna



def autostrada( T, k ):
    n = len(T)
    sumy = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        sumy[i][i] = T[i]

    for i in range(n):
        for j in range(i+1, n):
            sumy[i][j] = sumy[i][j-1] + T[j]
    F = [[-1 for i in range(k)]for j in range(n)]

    # for line in sumy:
    #     print(line)
    return rek(F, sumy, k-1, n-1)


    return 0 

runtests ( autostrada,all_tests=True )