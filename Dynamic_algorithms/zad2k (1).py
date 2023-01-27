from zad2ktesty import runtests
def check(S, F, a, b):
    if F[a][b]!=0: return True
    if a==b or b<a: return True
    if S[a] == S[b] and check(S, F, a+1, b-1):
        F[a][b]=b-a+1
        return True




def palindrom( S ):
    print(S)
    n = len(S)
    F = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i, n):
            check(S, F, i, j)

    maks=0

    for i in range(n):
        for j in range(n):
            if F[i][j]>maks:
                a=i
                b=j
                maks=F[i][j]

    return S[a:b+1]


runtests ( palindrom )