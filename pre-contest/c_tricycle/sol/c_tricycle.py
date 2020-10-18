# Solution by Emma Neiss

L, N = map(int, input().split())

# initialisation
items = [0 for i in range(N)]
for i in range(N):
    items[i] = int(input()) + 1     # ajout d'une personne fictive dans le groupe pour respecter les distances

# --- Implémentation du sac à dos classique sans répétition
# RQ : on fait +1 à la taille du sac initiale (longueur de la section de route) pour prendre
# en compte les distances nécessaires :
# comme on fait +1 à la taille de chacun des N groupes, mais qu'il faut laisser
# seulement N-1 espaces entre les groupes, on fait également +1 sur la taille du sac
# pour compenser
#
# Pour plus d'infos sur l'algorithme utilisé, voir "0-1 Knapsack Problem"

sac = [0 for i in range(L+2)]   # "sac" de taille L+2 (cap. max de L+1, commence à 0)
sac[0] = 1          # initialisation du sac
for item in items:
    for taille in range(L+1, -1, -1):
        if sac[taille] > 0 and taille + item <= L+1:
            sac[taille + item] = 1

    if sac[L+1] == 1:
        break

if sac[L+1] == 1:
    print("OUI")
else:
    print("NON")

