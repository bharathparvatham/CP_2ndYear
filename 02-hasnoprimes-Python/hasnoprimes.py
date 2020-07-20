# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.

import math


def isPrime(num):
    for i in range(2, math.floor(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def fun_hasnoprimes(l):
    for numList in l:
        for num in numList:
            if isPrime(num):
                return False
    else:
        return True
