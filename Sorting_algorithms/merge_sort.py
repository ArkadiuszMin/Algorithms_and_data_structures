def merge(T , p, q, r):
    lewa = T[p:q+1]
    prawa = T[q+1:r+1]
    print(T)
    print(lewa)
    print(prawa)
    print()
    a = 0
    b = 0
    dlg1 = len(lewa)
    dlg2 = len(prawa)
    while a < dlg1 and b < dlg2:
        if lewa[a] < prawa[b]:
            T[p] = lewa[a]
            a+=1
        else:
            T[p] = prawa[b]
            b+=1
        p+=1

    while b<dlg2:
        T[p] = prawa[b]
        b+=1
        p+=1
    while a<dlg1:
        T[p] = prawa[a]
        a+=1
        p+=1

def merge_sort(T, p, r):
    q = (p+r)//2
    if p+1 == r:
        merge(T, p, q, r)
    elif p+1<r:
        merge_sort(T, p, q)
        merge_sort(T, q+1, r)
        merge(T, p, q, r)

T = [4, 8, 2, 21, 51, 3, 2, 9, 15, 61, 89, 10, 23, 552, 31, 51, 86, 73, 12, 21, 58, 71, 63, 5, 18, 9, 22]
merge_sort(T, 0, len(T)-1)
print(T)