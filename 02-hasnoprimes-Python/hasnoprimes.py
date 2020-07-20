# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
    for numList in l:
        for num in numList:
            if isPrime(num):
                return False
    else:
        return True
