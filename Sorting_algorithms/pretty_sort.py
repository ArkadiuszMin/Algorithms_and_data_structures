
def radix(T, indeks):
    n = len(T)
    B = [0 for i in range(n)]
    C = [0 for i in range(10)]
    for x in T:
        C[x[indeks]] += 1
    if indeks == 2:
        for i in range(1, 10):
            C[i]+=C[i-1]
    if indeks == 1:
        for i in range(8, 0, -1):
            C[i]+=C[i+1]


    for i in range(n-1, -1, -1):
        B[C[T[i][indeks]]-1] = T[i]
        C[T[i][indeks]]-=1
    for i in range(n):
        T[i] = B[i]

def count(T):
    n = len(T)
    for i in range(n):
        liczba = T[i]
        tablica = [0 for i in range(10)]
        while liczba != 0:
            tablica[liczba%10]+=1
            liczba//=10
        jedno = 0
        wielo = 0
        for x in tablica:
            if x==1: jedno+=1
            if x>1: wielo+=1
        T[i] = (T[i], jedno, wielo)



def pretty(T):
    n = len(T)
    count(T)
    print(T)
    radix(T, 2)
    radix(T, 1)
    print(T)
    for i in range(n):
        T[i] = T[i][0]

T = [123, 455, 1266, 114577, 2344, 67333]
pretty(T)
print(T)