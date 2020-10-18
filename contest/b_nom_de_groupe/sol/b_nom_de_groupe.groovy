def reader = System.in.newReader()
def groupName = reader.readLine()

boolean isVowel(String c) {
    c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y'
}

def nbVowels = groupName.iterator().count { isVowel(it) }
def nbConsonants = groupName.length() - nbVowels

def score = 2 * nbVowels - nbConsonants

if (groupName.contains("ker")) {
    score += 5
}

if (score > 0 && groupName == groupName.reverse()) {
    score *= 2
}

println(score)
