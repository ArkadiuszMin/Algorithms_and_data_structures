#niech k = 6
def countsort(T, k):
    n = len(T)
    B = [0 for i in range(n)]
    C = [0 for i in range(k)]
    for x in T:
        C[x]+=1
    for i in range (1, k): #kumulacja
        C[i]+=C[i-1]
    for i in range(n):
        B[C[T[i]] - 1] = T[i]
        C[T[i]]-=1
    for i in range(n):
        T[i]=B[i]

T = [1, 0, 5, 3, 2, 3, 4, 0, 1, 2, 4, 3, 5, 0, 1, 0, 2, 4, 5, 3, 2, 1, 0, 3, 5, 4, 1, 2, 5, 3]
countsort(T, 6)
print(T)
