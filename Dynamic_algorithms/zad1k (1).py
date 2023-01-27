from zad1ktesty import runtests

def roznica( S ):
    n = len(S)
    F = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        if S[i]=='0':
            F[i][i]=1
        else:
            F[i][i]=-1

    # for line in F:
    #     print(line)

    for i in range(n):
        for j in range(i+1, n):
            if S[j]=='0':
                F[i][j]=F[i][j-1]+1
            else:
                F[i][j]=F[i][j-1]-1

    maks = -1

    for i in range(n):
        for j in range(i, n):
            if F[i][j]>maks:
                maks = F[i][j]
                a = i
                b = j





    return maks

runtests ( roznica )