# Solution by Sebastien Goll

def main():
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

    k = 0

    # boucle parcourant chaque rang
    for i in range(nr):
        # parcours des sieges au rang i
        for _ in range(nspr[i]):
            # verification du niveau d'audition de la personne
            if napp[k] >= i + 1:
                # si elle peut etre placee, on la sort de la liste a placer
                k += 1

                # on s'arrete s'il n'y a plus personne a placer
                if k == len(napp):
                    print("POSSIBLE")
                    return
            else:
                print("IMPOSSIBLE")
                return
    if k == len(napp):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")


main()