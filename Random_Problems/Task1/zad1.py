#ARKADIUSZ MINCBERGER
#Zaproponowany algorytm dla k < 11 stosuje insert sorta ktory patrzy k elementow w tyl (bo maks tyle w tyle bedzie dany element) i ma zlozonosc nk
#dla k>1 stosuje heap sorta (dla odwroconego kopca), gdzie wrzuca k elementow do tablicy, na poczatku buduje kopiec a nastepnie wyciaga najmniejszy element z kopca, doklada do istniejacej listy,
#zastepuje go kolejnym elementem z listy i jeszcze raz naprawia kopiec. Tak robi do momentu wrzucenia wszystkich elementow do tablicy i na sam koneic sortuje kopiec oraz
#przypina elementy z tablicy od tylu bo z racji odwroconego kopca posortowany wynik bedzie malejacy. zlozonosc to nlog(k+1)
#wspolczynnik k=11 zostal wyznaczony doswiadczalnie
#dla k = Teta(1) - f(x) = Teta(n)
#dla k = Teta(log(n)) - f(x) = Teta(nlog(log(k+1))
#dla k = Teta(n) - f(x) = Teta(nlog(k+1))

from zad1testy import Node, runtests

### SEKCJA INSERTA

def remove(p, q):
    p.next = q



### SEKCJA HEAPA

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2


def heapify(A, n, i):
    maks=i
    if left(i)<n and A[left(i)].val<A[maks].val:
        maks=left(i)
    if right(i)<n and A[right(i)].val<A[maks].val:
        maks=right(i)
    if maks != i:
        A[i], A[maks] = A[maks], A[i]
        return heapify(A, n, maks)

def build_kopiec(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def heap_sort(A, q):
    A.append(q)
    n=len(A)
    for i in range(n-2, -1, -1):
        A[i], A[0] = A[0], A[i]
        A[i+1].next=A[i]
        heapify(A, i, 0)




def SortH(p,k):

    if k<11:
        guardian = Node()
        guardian.next = p
        prev = guardian.next
        cur = guardian.next.next
        for i in range(k - 1):
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            else:
                first = guardian
                remove(prev, cur.next)
                while cur.val > first.next.val:
                    first = first.next
                cur.next = first.next
                first.next = cur
                cur = prev.next
        first = guardian
        while cur is not None:
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
            else:
                wstaw = first
                remove(prev, cur.next)
                while cur.val > wstaw.next.val:
                    wstaw = wstaw.next
                cur.next = wstaw.next
                wstaw.next = cur
                cur = prev.next
            first = first.next
        return guardian.next
    else:
        guardian = Node()
        q=guardian
        guardian.next=p
        A=[None for i in range(k)]
        for i in range(k):
            A[i]=p
            p=p.next
        if p is not None:
            A.append(p)
            p=p.next
        build_kopiec(A)
        q.next=A[0]
        while p is not None:
            q.next=A[0]
            A[0]=p
            p=p.next
            heapify(A, k+1, 0)
            q=q.next
        heap_sort(A,q)
        A[0].next=None

        return guardian.next
    # Zrob jutro, ogolne problemy sa takie ze calosc dziala git ale z racji ze na gorze listy mamy najmniejszy element to potem sort uklada je malejaca






    # tu prosze wpisac wlasna implementacje

runtests( SortH )