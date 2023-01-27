# ARKADIUSZ MINCBERGER
# Program pobiera energie z 0 pola i patrzy gdzie najdalej moze skoczyc. Wybiera pole z najwieksza iloscia ropy(energii) dostepne, skacze tam, dodaje energie
# a nastepnie dodaje do kolejki priorytetowej nowe pola na ktore moze skoczyc. Znowu patrzy na pole z najwieksza iloscia energii i je bierze. Jezeli
# jest ono za obecna pozycja po prostu dodaje energie do obecnej i nie wykonuje skoku (tak jakby skoczyl na nie juz wczesniej), jesli przed polem, skacze tam
# oblicza ile energii bedzie mial po skoku i znowu dodaje nowe pola do kolejki priorytetowej. Program konczy dzialanie w momencie kiedy jest w stanie wykonac
# skok na ostatnie pole. Program działa bo wykonuje najbardziej optymalne ruchy za kazdym razem (dopoki nie moze doskoczyc na koniec, to gdzies i tak musi skoczyc
# a najlepiej skoczyc na pole z najwieksza iloscia energii, jesli jakies pominelismy to i tak do niego wrocimy potem)
# Zlozonosc: O(nlog(n)), gdzie n to przejscie po tablicy T, a log(n) to branie elementu z kolejki

from zad5testy import runtests

import queue



def plan(T):
    n=len(T)
    wziete=[0]
    energia=0
    fura=0
    it=0
    q = queue.PriorityQueue()
    energia+=T[0]
    for i in range(T[0]):
        it+=1
        q.put((-T[it], it))
    while not ((n-1) - fura)<=energia:
        energ, indeks = q.get()
        energ*=(-1)
        wziete.append(indeks)
        if indeks>fura:
            skok=fura-indeks+energ
            fura=indeks
        else:
            skok=energ
        for i in range(energ):
            it+=1
            if it >= n:
                break
            q.put((-T[it], it))
        energia+=skok
    wziete.sort()
    return wziete





runtests( plan, all_tests = True )