# Solution by Sebastien Goll & Louis Hasenfratz

import collections

MAX_CARTE = 14

# taille du sac
taille_sac = int(input())
# nombre de cartes
nombre_cartes = int(input())


# dico de carte
cartes = {}
for i in range(1, MAX_CARTE + 1):
    cartes[i] = 0
for i in input().split():
    cartes[int(i)] += 1

# c le sac
sac_possible = [0 for i in range(taille_sac + 1)]
dicos = [[] for i in range(taille_sac + 1)]

# initialisation du dico de 0 a un dico full de 0
dicos[0].append({})
for i in range(1, MAX_CARTE + 1):
    dicos[0][0][i] = 0

sac_possible[0] = 1

# parcours de toutes les valeurs de carte possible
for valeur_carte in range(1, MAX_CARTE + 1):

    # parcours de toutes les cartes avec la valeur valeur_carte
    for nombre_valeur in range(cartes[valeur_carte]):

        # parcours des tailles de sac à dos
        for taille in range(taille_sac, -1, -1):

            # verification de la réalisabilité du sac à dos
            if taille + valeur_carte <= taille_sac and sac_possible[taille] == 1:

                sac_possible[taille + valeur_carte] = 1

                for dico_precedent in dicos[taille]:

                    new_dico = dico_precedent.copy()

                    new_dico[valeur_carte] += 1

                    for dico_suivant in dicos[taille + valeur_carte]:

                        if new_dico == dico_suivant:
                            break

                    else:
                        dicos[taille + valeur_carte].append(new_dico)

if not sac_possible[taille_sac]:
    print("NON")
else:
    for dico_max in dicos[taille_sac]:

        full_carte_copie = cartes.copy()
        for i in range(1,taille_sac+1):
            sac_possible[i]=0

        # on enleve le set permettant d'arriver au KP max du set de base
        for i in range(1, MAX_CARTE + 1):
            full_carte_copie[i] -= dico_max[i]

        for valeur_carte in range(1, MAX_CARTE + 1):

            # parcours de toutes les cartes avec la valeur valeur_carte
            for nombre_valeur in range(full_carte_copie[valeur_carte]):

                # parcours des tailles de sac à dos
                for taille in range(taille_sac, -1, -1):

                    # verification de la réalisabilité du sac à dos
                    if taille + valeur_carte <= taille_sac and sac_possible[taille] == 1:
                        sac_possible[taille + valeur_carte] = 1
        if not sac_possible[taille_sac]:
            print("OUI")
            break
    else:
        print("NON")
