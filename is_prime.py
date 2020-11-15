import math

def is_prime(x):

    is_prime = True

    last = int(math.sqrt(x))

    for i in range(2, last):
        if (x % i == 0):
            is_prime = False
            break

    if (is_prime == True):
        print(x, " is prime")

    return is_prime

is_prime(14197)
is_prime(4937)
is_prime(4939)