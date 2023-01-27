

def counting(T, indeks):
    n = len(T)
    B = [0 for i in range(n)]
    C = [0 for i in range(26)]
    for x in T:
        C[ord(x[indeks])-ord('a')]+=1
    for i in range(1, 26):
        C[i]+=C[i-1]
    for i in range(n-1, -1, -1):
        B[C[ord(T[i][indeks]) - ord('a')]-1]=T[i]
        C[ord(T[i][indeks])-ord('a')]-=1

    for i in range(n):
        T[i]=B[i]

def sort(T):
    max_ind = 0
    for x in T:
        if len(x) > max_ind:
            max_ind = len(x)
    buckets = [[] for i in range(max_ind)]
    for x in T:
        buckets[len(x)-1].append(x)

    for i in range(max_ind-1, 0, -1):
        counting(buckets[i], i)
        buckets[i-1].extend(buckets[i])

    counting(buckets[0], 0)
    for i in range(len(T)):
        T[i]=buckets[0][i]


T=["aba", "abba", "cbac", "ab", "ba", "acca", "bbac", "cbac", "babaa", "bbb", "baa", "caab", "bacb", "bab", "abbaagba"]
sort(T)
print(T)
