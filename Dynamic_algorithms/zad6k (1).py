from zad6ktesty import runtests 

def haslo ( S ):
    n = len(S)
    F = [0 for i in range(n)]
    if S[0]=='0': return 0
    F[0]=1
    if S[1]=='0' and ord(S[0])<ord('3'): F[1]=1
    elif S[1]=='0' and S[0]>=3: F[1]=0
    elif ord(S[0])>ord('2'): F[1]=1
    elif S[0]=='2' and ord(S[1])>ord('6'): F[1]=1
    else: F[1]=2

    for i in range(2, n):
        if S[i]!='0':
            F[i]+=F[i-1]
        if (S[i-1]=='1' or (S[i-1]=='2' and ord(S[i]) < ord('7'))):
            F[i]+=F[i-2]
    return F[n-1]

runtests ( haslo )