# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math


def isPrime(number):
    if number == 0 or number == 1:
        return False

    for num in range(2, math.floor(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def primeNumberInRange(number):
    if number == 0 or number == 1:
        return []
    primes = []
    for num in range(2, number + 1):
        if isPrime(num):
            primes.append(num)
    return primes


def primeFactors(number):
    factors = []
    primes = primeNumberInRange(number)
    index = 0
    while number > 1:
        if number % primes[index] == 0:
            factors.append(primes[index])
            number = number // primes[index]
        else:
            index += 1
    return list(set(factors))


def nthpowerfulnumber(n):
    # Your code goes here
    count = 0
    powerfulNumber = 1
    start = 2
    while count < n:
        factorsPrime = primeFactors(start)
        flag = True
        for factor in factorsPrime:
            if start % (factor ** 2) != 0:
                flag = False
                break
        if flag:
            count += 1
            powerfulNumber = start
        start += 1

    return powerfulNumber
