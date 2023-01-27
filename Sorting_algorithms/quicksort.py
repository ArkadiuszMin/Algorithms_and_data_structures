def partition(T, p, r):
    i = p
    x = T[r]
    for j in range(p, r):
        if T[j]<=x:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[r], T[i] = T[i], T[r]
    return i

def quicksort(T, p, r):
    while p<r:
        q = partition(T, p, r)
        quicksort(T, p, q-1)
        p=q+1



def selection(T, p, k, r):
    if p==r: return T[p]
    #if p<r:
    q = partition(T, p, r)
    if q==k: return T[q]
    if q<k: return selection(T, q+1, k, r)
    else: return selection(T, p, k, q-1)

T = [4, 8, 2, 21, 51, 3, 2, 9, 15, 61, 89, 10, 23, 552, 31, 51, 86, 73, 12, 21, 58, 71, 63, 5, 18, 9, 22]
quicksort(T, 0, len(T)-1)
print(T)