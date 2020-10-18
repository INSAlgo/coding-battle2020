# Solution by Louis Gombert ＼(º □ º l|l)/

import copy

n,m = map(int, input().split())

grid = [list(input()) for _ in range(n)]
total_line = list(map(int, input().split()))
total_col = list(map(int, input().split()))

n_manquant = [total_line[i] - grid[i].count("-") for i in range(n)]
m_manquant = [total_col[i] - [grid[j][i] for j in range(n)].count("-") for i in range(m)]

missing = sum(n_manquant) # == sum(m_manquant)
copy_grid = []

# Firstly, search for lines or columns that have to be completed with all -
for line in range(n):
    if total_line[line] == m: # if the line is only -, therefore the checksum of the line is equal to n
        for col in range(m):
            if grid[line][col] == "*":
                grid[line][col] = "-"
                n_manquant[line] -= 1
                m_manquant[col] -= 1

# Same for columns
for col in range(m):
    if total_col[col] == n:
        for line in range(n):
            if grid[line][col] == "*":
                grid[line][col] = "-"
                n_manquant[line] -= 1
                m_manquant[col] -= 1

missing = sum(n_manquant) # == sum(m_manquant)

# Fonction récursive de backtrack
def rec(missing, startl, startc):
    if missing == 0:
        global copy_grid
        copy_grid = copy.deepcopy(grid)
        return 1

    nb_completed = 0
    for line in range(startl, n):
        if n_manquant[line] > 0:
            for col in range(m):
                if line == startl and col < startc:
                    continue
                
                if m_manquant[col] > 0 and grid[line][col] != "-":
                    grid[line][col] = "-"
                    n_manquant[line] -= 1
                    m_manquant[col] -= 1

                    nb_completed += rec(missing-1, line, col)
                    

                    #
                    if nb_completed >= 2:
                        return 2
                    #

                    grid[line][col] = "*"

                    n_manquant[line] += 1
                    m_manquant[col] += 1
    
    return nb_completed


if rec(missing, 0, 0) == 1:
    print('\n'.join(''.join(copy_grid[i]) for i in range(n)))
else:
    print("NON")
