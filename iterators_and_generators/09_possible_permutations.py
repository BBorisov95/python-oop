from itertools import permutations

def possible_permutations(ls):
    for perm in permutations(ls):
        yield list(perm)

