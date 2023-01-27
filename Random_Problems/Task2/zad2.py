#ARKADIUSZ MINCBERGER
#Algorytm najpierw sortuje przedziały quicksortem, wedle pierwszej współrzędnej rosnąco, a drugorzędnie malejąco wedle drugiej współrzednej.
#Nastepnie przechodzi przez wszystkie elementy tablicy L i robi liste potencjalnych kandydatow ktorzy moga zawierać w sobie najwięcej
#przedziałów (Pierwszy element z nową pierwszą współrzędna jest potencjalnym kandydatem, o ile jego druga współrzędna jest większa niż dotychczasowa
#najwieksza druga wspolrzedna). Nastepnie sprawdza każdego kandydata, zaczyanjac liczenie od kolejnego kandydata (do kolejnego kandydata pożre wszystko)
#dopóki liczba pożartych przez niego przedziałów będzie większa niż potencjalna liczba pożartych przedziałów niesprawdzonych kandydatów (no albo do końca)
#algorytm co prawda posiada petle w petli co w pesymistycznym przypadku daje zlozonosc nlogn + n^2 natomiast przez sprawdzanie malej ilosci elementow i
#przerwanie petli w odpowiednim momencie zloznosc szacunkowa to nlogn + n



from zad2testy import runtests

def quick_sort(a, p, r):
  while p<r:
    q = podzial(a, p, r)
    quick_sort(a, p, q-1)
    p=q+1

def podzial(a, p, r):
  x=a[r][0]
  y=a[r][1]
  i=p-1
  for j in range(p, r):
    if a[j][0] < x or (a[j][0]==x and a[j][1] >=y):
      i+=1
      a[i], a[j] = a[j], a[i]
  a[i+1], a[r] = a[r], a[i+1]
  return i+1


def depth(L):
    n = len(L)
    quick_sort(L, 0, n - 1)
    maks = L[0][1]
    b = L[0][1]
    count = 0
    maks_count = 0
    tab = []
    for i in range(1, n):
        if b >= L[i][1]:  # cos czuje ze da sie szybciej
            maks_count += 1
        elif L[i][1] > maks:
            tab.append(i)  # tu sa pierwsze elementy roznych wartych sprawdzenia
            maks = L[i][1]
    m = len(tab)
    for i in range(m - 1):
        indeks= tab[i] #indeks
        b = L[indeks][1] #druga wspolrzedna
        count = tab[i + 1] - (tab[i] + 1)
        for j in range(tab[i + 1] + 1, n):
            if b >= L[j][1]:
                count += 1
        if count > maks_count:
            maks_count = count
        if maks_count > n-1 - tab[i+1]:
            return maks_count
    count = n - 1 - tab[m - 1]
    if maks_count < count:
        maks_count = count
    return maks_count


runtests( depth )