def parent(x):
    return (x-1)//2

def left(x):
    return 2*x + 1

def right(x):
    return 2*x + 2

def heapify(T ,n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and T[l] > T[max_ind]:
        max_ind = l
    if r < n and T[r] > T[max_ind]:
        max_ind = r
    if max_ind != i:
        T[i], T[max_ind] = T[max_ind], T[i]
        heapify(T, n, max_ind)

def build_heap(T):
    n = len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)

def heap_sort(T):
    n = len(T)
    build_heap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)


T = [4, 8, 2, 21, 51, 3, 2, 9, 15, 61, 89, 10, 23, 552, 31, 51, 86, 73, 12, 21, 58, 71, 63, 5, 18, 9, 22]
heap_sort(T)
print(T)

