def reader = System.in.newReader()

def nbbillets = reader.readLine() as int
def prix1 = reader.readLine() as int
def prix2 = reader.readLine() as int
def prix3 = reader.readLine() as int

if (nbbillets > 200) {
    nbbillets = nbbillets - 200
    println(nbbillets * prix3 + 100 * prix2 + 100 * prix1)
} else if (nbbillets > 100) {
    nbbillets = nbbillets - 100
    println(nbbillets * prix2 + 100 * prix1)
} else {
    println(nbbillets * prix1)
}
