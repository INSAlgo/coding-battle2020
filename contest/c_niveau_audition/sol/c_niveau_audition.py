# Solution by Sebastien Goll

"""
Recuperation des entrees:
nr: le nombre de rangs disponibles
nspr: une liste de taille nr avec chaque element decrivant le nombre de siege sur le rang correspondant
np: le nombre de personnes
napp: une liste de taille np indiquant le niveau d'audition de chaque personne
"""
nr = int(input())
nspr = [int(i) for i in input().split()]
np = int(input())
napp = [int(i) for i in input().split()]

napp.sort()
impossible = False

# boucle parcourant chaque rang
for i in range(nr):
    
    if impossible:
        break
    # Verification: est-ce qu'il reste des gens a placer ?
    if len(napp) > 0:

        # parcours des sieges au rang i
        for j in range(nspr[i]):

            # verificatrion du niveau d'audition de la personne
            if napp[0] >= i + 1:

                # si elle peux etre place, on la sort de la liste a placer
                napp.pop(0)

                # on s'arrete si il n'y a plus personne a placer
                if len(napp) == 0:
                    break
            else:
                print("IMPOSSIBLE")
                impossible = True
                break
if not impossible:
    if len(napp) == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
