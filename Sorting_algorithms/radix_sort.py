def counting(T, l):
    n = len(T)
    B = [0 for i in range(n)]
    C = [0 for i in range(26)]
    for x in T:
        C[ord(x[l])-ord('a')]+=1
    for i in range(1, 26):
        C[i]+=C[i-1]
    for i in range(n-1, -1, -1):
        B[C[ord(T[i][l])-ord('a')]-1]=T[i]
        C[ord(T[i][l])-ord('a')]-=1
    for i in range(n):
        T[i]=B[i]

def radix(T):
    n = len(T[0])
    for i in range(n-1, -1, -1):
        counting(T, i)


T = ["adbac", "abbac", "aaaaa", "baabd", "dbaca", "acbad", "baaca", "bcaab", "baaaa", "ababa", "barca", "cabca", "ccccc", "aabaa", "cacac"]
radix(T)
print(T)

