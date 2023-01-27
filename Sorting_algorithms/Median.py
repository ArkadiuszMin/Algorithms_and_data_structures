from zad1testy import runtests

def particion(T, p, r):
    i = p-1
    x = T[r]
    for j in range(p, r):
        if T[j]<=x:
            i+=1
            T[i], T[j] = T[j], T[i]
    T[r], T[i+1] = T[i+1], T[r]
    return i+1

def selection(T, p, k, r):
    if p==r: return p
    if p<r:
        q = particion(T, p, r)
        if q==k: return q
        if q<k: return selection(T, q+1, k, r)
        else: return selection(T, p, k, q-1)


def Median(T):
    n = len(T)
    liniowka = [0 for i in range(n*n)]
    for i in range(n):
        for j in range(n):
            liniowka[n*i + j]=T[i][j]
    mala = selection(liniowka, 0, (n*n - n)/2, n*n-1 )
    duza = selection(liniowka, 0, (n*n -n)/2 + n - 1, n * n - 1)
    # print(liniowka)
    # print(mala)
    # print(duza)
    malutka = mala - 1
    wielka = duza + 1
    for i in range(1, n):
        for j in range(0, i):
            T[i][j]=liniowka[malutka]
            malutka-=1
    for i in range(0, n):
        for j in range(i+1, n):
            T[i][j]=liniowka[wielka]
            wielka+=1
    for i in range(0, n):
        T[i][i]=liniowka[mala]
        mala+=1


    return T

runtests( Median )
