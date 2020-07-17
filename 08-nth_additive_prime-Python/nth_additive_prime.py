# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

import math


def isPrime(number):
    for index in range(2, math.floor(number ** 0.5) + 1):
        if number % index == 0:
            return False
    return True


def primesInRange(start, end):
    primes = []
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    return primes


def sumOfDigits(number):
    result = 0
    while number > 0:
        result += number % 10
        number = number // 10
    return result


def fun_nth_additive_prime(n):
    additivePrimes = [2, 3, 5, 7]

    if n < len(additivePrimes) - 1:
        return additivePrimes[n]
    else:
        start = 8
        while len(additivePrimes) - 1 < n:
            primes = primesInRange(start, start + 20)
            for prime in primes:
                if isPrime(sumOfDigits(prime)):
                    additivePrimes.append(prime)
                    if len(additivePrimes) - 1 == n:
                        break
            start += 21
        return additivePrimes[n]
