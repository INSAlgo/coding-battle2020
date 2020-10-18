# Solution by Sebastien Goll

Nb =  int(input())
P1 =  int(input())
P2 = int(input())
P3 = int(input())

somme = 0
if Nb <= 100:
    print(Nb * P1)
else:
    Nb -= 100
    somme += 100 * P1

    if Nb <= 100:
        print(somme+Nb * P2)
    else:
        Nb -= 100
        print(somme + 100 * P2 + Nb * P3)
