# Solution by Emma Neiss

VOWELS = {'a', 'e', 'i', 'o', 'u', 'y'}

def palindrome(name):
    """
    Returns true if name is a palindrome (equals itself reversed)
    """
    return name == name[::-1]


def score(name):
    """
    Returns the score of name, using the rules defined in the subject
    """
    score = 0

    # unique bonus if name contains 'ker' at least once
    if name.count('ker') >= 1:
        score += 5

    # difference between voy and cons
    cons = 0
    voy = 0
    for char in name:
        if char in VOWELS:
            voy += 1
        else:
            cons += 1

    score += 2*voy - cons

    if palindrome(name) and score > 0:
        score *= 2

    return score


# read input & compute score
print(score(input()))
