from zad8ktesty import runtests 

def napraw ( s, t ):

    n = len(s)
    m = len(t)
    F = [[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(n+1):
        F[0][i] = i
    for i in range(m+1):
        F[i][0]=i
    for i in range(1, m+1):
        for j in range(1, n+1):
            if t[i-1]==s[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j-1], F[i-1][j], F[i][j-1])+ 1#zamianka/dodanie/skasowanie

    return F[m][n]

runtests ( napraw )