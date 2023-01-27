#T - tablica, m - ilosc rzedow, k - ilosc ludzi w kazdym rzedzie
# Numeracja:              0   3   6   9   12   14
#                           1   4   7   10   13
#                             2   5   8    11




def partition(T, p, r):
    x = T[r][1]
    i = p-1
    for j in range(p, r):
        if T[j][1]>=x:
            i+=1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def selection(T, p, r, k):
    if p==r: return
    q = partition(T, p, r)
    if k == q: return
    elif k < q:
        selection(T, p, q-1, k)
    else:
        selection(T, q+1, r, k)

def zdjecie(T, m, k):
    n = len(T)
    wynik = [0 for i in range(n)]
    miejsca = [0 for i in range(m)]
    k2 = k
    miejsce = n-k2

    for i in range(m):
        miejsca[i]=miejsce
        k2+=1
        miejsce-=k2
    prev = n-1

    for x in miejsca:
        selection(T, 0, prev, x)
        prev = x-1

    start = m-1
    ilosc = k

    for x in miejsca:
        skok = m
        pozycja = start
        for i in range(x, x+k):
            wynik[pozycja] = T[i]
            pozycja+=skok

        for i in range(x+k, x+ilosc):
            wynik[pozycja] = T[i]
            skok-=1
            pozycja+=skok

        start-=1
        ilosc+=1


    for i in range(n):
        T[i] = wynik[i]

    return None

T = [(48, 26), (82, 42), (24, 65), (28, 17), (14, 62), (72, 74), (26, 55), (88, 7), (2, 41), (8, 45), (68, 36), (50, 14), (64, 79), (38, 33), (54, 48)]
zdjecie(T, 3, 4)
print(T)