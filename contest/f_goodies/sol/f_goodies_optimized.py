# Solution by ArnaudF
# Largely inspired by the solution from Sebastien Goll & Louis Hasenfratz
import collections
from collections import defaultdict

Q = int(input())
N = int(input())
# The goodies are sorted to make sure that two goodies of the same price are grouped together.
# This is useful when constructing combinations, line 27-29.
goodies = sorted(list(map(int, input().split())))

#Sac definition
bag = defaultdict(set)
bag[0].add(tuple())

#List substration. Does the same as the - operator with sets.
# list1 = [1,2,3,4,5]; list2 = [4,5]
# Return: [1,2,3]
def diff(list1, list2):
	for element in list2:
		list1.remove(element)
	return list1

#Build all the possible combinations that give a bag size from 0 to Q.
for card in goodies:
	for size in range(Q+1, -1 , -1):
		if size + card <= Q and size in bag:
			for combinaison in bag[size]:
				combinaison = combinaison + (card,)
				bag[size+card].add(combinaison)

#For each combination that gives the desired sum Q, 
# the combination is removed from the goodies list. 
# Then we check whether it is still possible to build a bag with a price Q.
# If not: We win, print "OUI"
weWin = False
for combinaison in bag[Q]:
	newgoodiesList = diff(goodies.copy(), combinaison)
	newbag = defaultdict(bool)
	newbag[0] = True
	for card in newgoodiesList:
		for size in range(Q+1, -1 , -1):
			if size + card <= Q and size in newbag:
				newbag[size+card] = True
	if Q not in newbag:
		weWin = True
		break

if weWin:
	print("OUI")
else:
	print("NON")