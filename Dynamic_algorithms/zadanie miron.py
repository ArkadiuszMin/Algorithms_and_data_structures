class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.F = None


def przygotuj(s, k):
    s.F=[0 for i in range(k+1)]
    if s.left is not None:
        przygotuj(s.left, k)
    if s.right is not None:
        przygotuj(s.right, k)

def odpal(p, k):
    rek(p, k)
    if p.left is not None:
        odpal(p.left, k)
    if p.right is not None:
        odpal(p.right, k)

def sprawdz(p, k):
    if p == None:
        return 0
    return max(p.F[k], sprawdz(p.left, k), sprawdz(p.right, k))


def rek(p, k):
    if k==0 or p.left == None and p.right == None:
        return 0

    if p.F[k] != 0:
        return p.F[k]

    lewy = 0
    prawy = 0
    srodek = 0

    if p.left is not None:
        lewy = rek(p.left, k-1) + p.leftval
    if p.right is not None:
        prawy = rek(p.right, k-1) + p.rightval

    if p.right is not None and p.left is not None:
        for j in range(k-1):
            srodek = max(srodek, rek(p.left, k-2-j) + p.leftval + rek(p.right, j) + p.rightval)

    p.F[k] = max(lewy, srodek, prawy)
    return p.F[k]




def valuableTree(T, k):
    przygotuj(T, k)
    odpal(T, k)
    return sprawdz(T, k)



