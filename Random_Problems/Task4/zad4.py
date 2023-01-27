# ARKADIUSZ MINCBERGER
# Algorymt dziala w sposob takowy, ze najpierw sortuje sobie tablice T budynkow, wedle wspolrzednej b, a nastepnie zaklada budowe kazdego z nich i patrzy jaka jest maks liczba studentow
# ktora moze byc zmieszczona do wszystkich budynkow przy zalozeniu ze i-ty jest budowany. Dziala to w ten sposob ze wybieram i-ty budynek, a nastepnie patrze
# na wszystkie poprzednie, i jezeli koszt jakiegos poprzedniego nie przekracza kosztu obecnego pomniejszonego i koszt i-tego budynku
# oraz jego wspolrzedna b jest przed wspolrzedna a, to sprawdzam rekurencyjnie czy dodanie do i-tego, j-tego da mi najwieksza pojemnosc.
# W tablicy F przechowuje ilosc studentow mozliwe do pomieszczenia do i-tego budynku oraz do k-tego kosztu, oraz budynek budowany zaraz przed i-tym (i koszt jaki mi zostaje)
# Nastepnie po znalezieniu budynku przy ktorym zbudowaniu jako ostatnim mam najwieksza ilosc studentow, cofam sie rekurencyjnie
# uzywajac informacji o budynku budowanym zaraz przed i-tym oraz jego koszcie (wiem dzieki temu dokladnbie jaki krok rekurencyjny zostal wykonany wczesniej)
# Zlozonosc obliczeniowa algorytmu wynosi O(k*n^2), gdyz tablica F ma wymiary k na n i przy najgorszym przypadku zapełnie ja całą i dla kazdego i-tego elementu
# tablicy T, cofam sie i budynkow wstecz, co w notacji O daje k*n*n

from zad4testy import runtests

def studenci(T, F, pocz, k, i):

    if F[i][k][0] != 0:
        return F[i][k][0]

    if T[i][3] > k:
        return 0

    ludzie = T[i][0]*(T[i][2]-T[i][1])
    F[i][k][0]=ludzie

    for j in range(i):
        if T[j][2] < pocz and T[j][3]<=k-T[i][3]:
            if studenci(T, F, T[j][1], k-T[i][3], j) + ludzie > F[i][k][0]:
                F[i][k][0] = studenci(T, F, T[j][1], k-T[i][3], j) + ludzie
                F[i][k][1] = (j, k-T[i][3])

    return F[i][k][0]




def select_buildings(T,p):
    n=len(T)
    for i in range(n):
        T[i]=(T[i][0], T[i][1], T[i][2], T[i][3], i)
    T = sorted(T, key=lambda x:x[2])

    F = [[[0,(0,0)] for _ in range(p+1)] for _ in range (n+1)]

    max_val = 0
    indeks=0

    for i in range(n):
        if studenci(T, F, T[i][1], p, i) > max_val:
            max_val=studenci(T, F, T[i][1], p, i)
            indeks=i


    budynki=[]
    hajs=p


    while F[indeks][hajs][0] != 0:
        budynki.append(T[indeks][4])
        indeks, hajs = F[indeks][hajs][1]


    budynki = sorted(budynki)



    return budynki

runtests( select_buildings )
