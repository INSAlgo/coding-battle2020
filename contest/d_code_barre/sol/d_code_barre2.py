# Solution by Emma Neiss

import sys

nb_lignes, nb_col = map(int, input().split())

solution = None     # variable globale pour stocker le resultat


# trouve toutes les positions possibles pour un '-'
def possible_dashes(matrix, missing_line, missing_col, startL, startC):
    possible = []

    # recherche de la case possible
    for line in range(startL, nb_lignes):
        if missing_line[line] > 0:
            for col in range(nb_col):
                if line == startL and col < startC:
                    continue
                if missing_col[col] > 0 and matrix[line][col] == '*':
                    possible.append((line, col))

    return possible


# ------------- BACKTRACKING
def count_sol(matrix, missing_line, missing_col, missing, startL, startC):
    global solution

    # cas d'arret
    if missing == 1:
        possibilites = possible_dashes(matrix, missing_line, missing_col, startL, startC)
        # stockage de la solution
        if len(possibilites) == 1:
            solution = [row[:] for row in matrix]
            solution[possibilites[0][0]][possibilites[0][1]] = '-'
        return len(possibilites)

    # recursion (else)
    possibilities = possible_dashes(matrix, missing_line, missing_col, startL, startC)
    sum = 0

    for line, col in possibilities:
        # on fait un choix possible
        matrix[line][col] = '-'
        missing_line[line] -= 1
        missing_col[col] -= 1
        missing -= 1

        # appel de recursion
        sum += count_sol(matrix, missing_line, missing_col, missing, line, col)

        if sum > 1:
            # on ne veut pas savoir combien il y a de possibilites,
            # seulement s'il y en a plus d'unr
            return sum

        # on defait le choix
        matrix[line][col] = '*'
        missing_line[line] += 1
        missing_col[col] += 1
        missing += 1

    return sum


# ------------- SUITE PARSING (oui c'est sale)
matrice = []
nb_tirets_lignes = [0 for _ in range(nb_lignes)]
nb_tirets_col = [0 for _ in range(nb_col)]

for i in range(nb_lignes):
    ligne = input()
    matrice.append(list(ligne))
    nb_tirets_lignes[i] = ligne.count('-')

    for col, car in enumerate(ligne):
        if car == '-':
            nb_tirets_col[col] += 1

# print(matrice)
# print(nb_tirets_lignes)
# print(nb_tirets_col)

# calcul tirets manquants
manquants_lignes = [0 for _ in range(nb_lignes)]
manquants_col = [0 for _ in range(nb_col)]
total_lignes = list(map(int, input().split()))
total_col = list(map(int, input().split()))

for l in range(nb_lignes):
    manquants_lignes[l] = total_lignes[l] - nb_tirets_lignes[l]

for c in range(nb_col):
    manquants_col[c] = total_col[c] - nb_tirets_col[c]


manquants = sum(manquants_lignes)

# =========== AJOUT EDGE CASE CODE DEJA BON
if manquants == 0:
    print('\n'.join(''.join(matrice[i]) for i in range(nb_lignes)))
    sys.exit(0)

# print(manquants_lignes)
# print(manquants_col)

# print(possible_dashes(matrice, manquants_lignes, manquants_col))

if count_sol(matrice, manquants_lignes, manquants_col, manquants, 0, 0) > 1:
    print("NON")
else:
    if solution is not None:
        print('\n'.join(''.join(solution[i]) for i in range(nb_lignes)))
    else:
        print("snif ca marche po :'(")

# fuck les doublons >.>
