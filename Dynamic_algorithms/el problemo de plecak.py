#P - wartosci przedmiotow
#W - waga przedmiotow
#k - pojemnosc plecaka

def plecak(P, W, k):
    n = len(P)
    F = [[0 for i in range(k+1)] for j in range(n)]
    wziete = [[False for i in range(k+1)]for j in range(n)]
    for i in range(W[0], k+1):
        F[0][i]=P[0]
        wziete[0][i]=True
    for i in range(1, n):
        for j in range(1, k+1):
            if j-W[i]>=0:
                if F[i-1][j-W[i]] + P[i] > F[i-1][j]:
                    wziete[i][j]=True
                F[i][j] = max(F[i-1][j], F[i-1][j-W[i]]+P[i])
            else:
                F[i][j] = F[i-1][j]

    pojemnosc = k
    item = n-1
    wynik =[]
    while pojemnosc > 0 and item >=0:
        if wziete[item][pojemnosc] == True:
            wynik.append(item)
            pojemnosc-=W[item]
        item-=1
        #print(pojemnosc, " ", item)

    cena = 0
    waga = 0
    for x in wynik:
        cena+=P[x]
        waga+=W[x]

    print(wynik)

    print(F[n-1][k])
    print(cena)
    print(waga)


W = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
P = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
W2 = [92, 4, 43, 83, 84, 68, 92, 82, 6, 44, 32, 18, 56, 83, 25, 96, 70, 48, 14, 58]
P2 = [44, 46, 90, 72, 91, 40, 75, 35, 8, 54, 78, 40, 77, 15, 61, 17, 75, 29, 75, 63]
plecak(P, W, 269)