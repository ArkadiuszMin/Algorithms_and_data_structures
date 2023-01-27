from zad7ktesty import runtests 
from queue import PriorityQueue

def drzewsko(T, x, wagi, i):
    n = len(T)
    m = len(T[0])
    PQ = PriorityQueue()
    waga=0
    PQ.put((0, x))
    while not PQ.empty():
        a, b = PQ.get()
        waga+=T[a][b]
        T[a][b]=0
        #print(a, b)
        if a+1 < n and T[a+1][b]!=0:
            PQ.put((a+1, b))
        if a-1 > 0 and T[a-1][b]!=0:
            PQ.put((a-1, b))
        if b + 1 < m and T[a][b+1]!=0:
            PQ.put((a, b+1))
        if b - 1 > 0 and T[a][b-1]!=0:
            PQ.put((a, b-1))
    wagi[i]=waga



def ogrodnik (T, D, Z, l):
    n = len(D)
    wagi = [0 for i in range(n)]
    for i in range(n):
        drzewsko(T, D[i], wagi, i)

    F=[[0 for i in range(l+1)] for j in range(n)]

    for i in range(wagi[0], l+1):
        F[0][i]=Z[0]

    for i in range(1, n):
        for j in range(1, l+1):
            if j - wagi[i] >= 0:
                F[i][j] = max(F[i-1][j], F[i-1][j-wagi[i]] + Z[i])
            else:
                F[i][j] = F[i-1][j]

    return F[n-1][l]


    return 0

runtests( ogrodnik, all_tests=True)
