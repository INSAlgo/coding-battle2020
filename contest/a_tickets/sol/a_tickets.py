# Solution by Louis Hasenfratz

nbbillets = int(input())
prix1=int(input())
prix2 = int(input())
prix3 = int(input())
tarif=0
if nbbillets>200:
    nbbillets=nbbillets-200
    print(nbbillets*prix3+100*prix2+100*prix1)
elif nbbillets>100:
    nbbillets = nbbillets - 100
    print(nbbillets * prix2 + 100 * prix1)
else :
    print(nbbillets * prix1)



