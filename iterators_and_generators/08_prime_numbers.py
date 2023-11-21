from math import sqrt

def get_primes(numbs: list):
    for num in numbs:
        if num < 2:
            continue
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            yield num

print(list(get_primes([100_000_000_000_007])))