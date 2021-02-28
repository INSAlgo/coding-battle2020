import copy

L,C = map(int, input().split())
grid = [list(input()) for _ in range(L)]
sumLine = list(map(int, input().split()))
sumRow = list(map(int, input().split()))
currentSumLine = [sumLine[i]-grid[i].count("-") for i in range(L)]
currentSumRow = [sumRow[j]-sum([grid[i][j].count("-") for i in range(L)]) for j in range(C)]

def result(grid, currentSumLine, currentSumRow, inversed=False):
	for i in range(L):
		if inversed:
			for j in range(C-1,-1,-1):
				if grid[i][j]=="*" and currentSumLine[i] > 0 and currentSumRow[j] > 0:
					grid[i][j] = "-"
					currentSumLine[i] -= 1
					currentSumRow[j] -= 1
		else:
			for j in range(C):
				if grid[i][j]=="*" and currentSumLine[i] > 0 and currentSumRow[j] > 0:
					grid[i][j] = "-"
					currentSumLine[i] -= 1
					currentSumRow[j] -= 1
	return grid

first = result(copy.deepcopy(grid), currentSumLine.copy(), currentSumRow.copy())
second = result(copy.deepcopy(grid), currentSumLine.copy(), currentSumRow.copy(), inversed=True)

def equal(tab1, tab2):
	for i in range(L):
		for j in range(C):
			if tab1[i][j] != tab2[i][j]:
				return False
	return True

print('\n'.join(''.join(first[i]) for i in range(L)))
print("oooooooooo")
print('\n'.join(''.join(second[i]) for i in range(L)))
print(sumLine, sumRow)
if equal(first, second):
    print('\n'.join(''.join(first[i]) for i in range(L)))
else:
    print("NON")
