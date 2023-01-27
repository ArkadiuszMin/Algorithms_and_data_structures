from zad9ktesty import runtests
from math import inf


def la_rekursja(P, F, d, g, indeks):





    #----------------------------------------#
    #                                        #
    #                                        #
    ### PODEJSCIE REKURENCYJNE (ZAJEBISTE) ###
    #                                        #
    #                                        #
    #----------------------------------------#

    if indeks>=len(P):
        return 0

    if F[indeks][g][d]!=-1:
        return F[indeks][g][d]

    if d - P[indeks] < 0 and g - P[indeks] < 0:
        return 0

    if d - P[indeks] >= 0 and g - P[indeks] >= 0:

        if la_rekursja(P, F, d-P[indeks], g, indeks+1) >  la_rekursja(P, F, d, g-P[indeks], indeks+1):
            F[indeks][g][d] = la_rekursja(P, F, d-P[indeks], g, indeks+1) + 1
            return F[indeks][g][d]

        if la_rekursja(P, F, d - P[indeks], g, indeks + 1) <= la_rekursja(P, F, d, g - P[indeks], indeks + 1):
            F[indeks][g][d] = la_rekursja(P, F, d, g - P[indeks], indeks + 1) + 1
            return F[indeks][g][d]


    if d - P[indeks] >= 0:

        F[indeks][g][d] = la_rekursja(P, F, d - P[indeks], g, indeks + 1) + 1
        return F[indeks][g][d]

    else:

        F[indeks][g][d] = la_rekursja(P, F, d, g - P[indeks], indeks + 1) + 1
        return F[indeks][g][d]


def prom(P, g, d):
    n = len(P)
    F = [[[-1 for i in range(d+1)]for j in range(g+1)]for k in range(n)]
    poklad_d = []
    poklad_g = []
    w1 = 0
    w2 = 0
    indeks=0

    g2 = g
    d2 = d

    while not(indeks>=len(P) or (d2 - P[indeks] < 0 and g2 - P[indeks] < 0)):

        if d2 - P[indeks] >= 0 and g2 - P[indeks] >= 0:

            w1 = la_rekursja(P, F, d2 - P[indeks], g2, indeks + 1)
            w2 = la_rekursja(P, F, d2, g2 - P[indeks], indeks + 1)

            if w1 > w2:
                poklad_d.append(indeks)
                d2 -= P[indeks]
            else:
                poklad_g.append(indeks)
                g2 -= P[indeks]



        elif d2 - P[indeks] >= 0:

            poklad_d.append(indeks)
            d2 -= P[indeks]

        else:

            poklad_g.append(indeks)
            g2 -= P[indeks]

        indeks+=1

    if poklad_d[len(poklad_d)-1]==indeks-1:
        return poklad_d
    return poklad_g






    #-------------------------------------#
    #                                     #
    #                                     #
    ### PODEJSCIE ITERACYJNE (CHUJOWE) ####
    #                                     #
    #                                     #
    #-------------------------------------#










    # print(P)
    # print(g)
    # print(d)
    # n = len(P)
    # F=[[[0 for i in range(g+1)]for j in range(d+1)]for k in range(n)]
    # wyniki = [[[-1 for i in range(g+1)]for j in range(d+1)]for k in range(n)]
    # for i in range(P[0], d+1):
    #     for j in range(g+1):
    #         F[0][i][j]=1
    #         wyniki[0][i][j] = 0
    # for i in range(P[0], g+1):
    #     for j in range(d+1):
    #         F[0][j][i]=1
    #         wyniki[0][j][i]=1
    #
    # for i in range(1, n):
    #     for j in range(d+1):
    #         for k in range(g+1):
    #             if j - P[i] >= 0:
    #                 if F[i-1][j-P[i]][k] != 0:
    #                     F[i][j][k] = F[i-1][j-P[i]][k]+1
    #                     wyniki[i][j][k]=0
    #             if k - P[i] >= 0:
    #                 if F[i-1][j][k-P[i]] != 0:
    #                     if j - P[i] >= 0:
    #                         if F[i-1][j-P[i]][k] > F[i-1][j][k-P[i]]:
    #                             F[i][j][k] = F[i-1][j-P[i]][k] + 1
    #                             wyniki[i][j][k] = 0
    #                         elif F[i-1][j-P[i]][k] < F[i-1][j][k-P[i]]:
    #                             F[i][j][k] = F[i-1][j][k-P[i]] + 1
    #                             wyniki[i][j][k] = 1
    #                     else:
    #                         F[i][j][k] = F[i-1][j][k-P[i]] + 1
    #                         wyniki[i][j][k] = 1
    # indeks = -1
    # for i in range(n-1, -1, -1):
    #     if F[i][d][g]!=0:
    #         indeks = i
    #         break
    #
    # if indeks == -1:
    #     return []
    # tablica = []
    # prawda = wyniki[indeks][d][g]
    #
    # while wyniki[indeks][d][g] != -1:
    #     if wyniki[indeks][d][g] == prawda:
    #         tablica.append(indeks)
    #     if wyniki[indeks][d][g] == 0:
    #         d-=P[indeks]
    #     else:
    #         g-=P[indeks]
    #     indeks-=1
    # s = len(tablica)
    # for i in range(s//2):
    #     tablica[i], tablica[s-1-i] = tablica[s - i - 1], tablica[i]
    #
    # return tablica



runtests ( prom )