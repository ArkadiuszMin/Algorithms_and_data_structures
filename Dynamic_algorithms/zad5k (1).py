from zad5ktesty import runtests

def ruch(A, F, a, b):
    if F[a][b] != 0:
        return F[a][b]
    if a==b:
        F[a][b]=A[a]
        return A[a]
    if a+1==b:
        F[a][b] = max(A[a], A[b])
        return F[a][b]
    F[a][b] = max(A[a] + min(ruch(A, F, a+2, b),ruch(A, F, a+1, b-1)), A[b] + min(ruch(A, F, a, b-2), ruch(A, F, a+1, b-1)))
    return F[a][b]



def garek ( A ):
    n = len(A)
    F = [[0 for i in range(n)] for j in range(n)]
    return ruch(A, F, 0, n-1)

runtests ( garek )