# Solution by Louis Hasenfratz

nbrouge,nbmarron=input().split()
nbtransports=int(input())
nbrouge=int(nbrouge)
nbmarron=int(nbmarron)
maxrouge=0
maxmarron=0
maxbus=0


for i in range(nbtransports):
    valeurscourante = input().split()
    if len(valeurscourante)==3:
        if (valeurscourante[1]=="r"):
            maxrouge=maxrouge+int(valeurscourante[2])
        else:
            maxmarron = maxmarron +int( valeurscourante[2])
    else :
        maxbus=maxbus+int(valeurscourante[1])

nbrougerestant=nbrouge-maxrouge if nbrouge-maxrouge>0 else 0
nbmarronrestant=nbmarron-maxmarron if nbmarron-maxmarron>0 else 0

nbrestant=nbrougerestant+nbmarronrestant-maxbus if maxbus<nbmarronrestant+nbrougerestant else 0
maxrouge=(maxrouge if nbrougerestant>0 else nbrouge)
maxmarron=(maxmarron if nbmarronrestant>0 else nbmarron)
print(nbrestant,maxrouge +maxmarron , maxbus if nbrestant>0 else nbrougerestant+nbmarronrestant  )
