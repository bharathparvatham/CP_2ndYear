# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
import math


def isPrime(number):
    for num in range(2, math.floor(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def listOfPrimes(number):
    primes = []
    for num in range(2, number + 1):
        if isPrime(num):
            primes.append(num)
    return primes


def sumOfDigits(number):
    digitsSum = 0
    while number > 0:
        digitsSum += (number % 10)
        number = number // 10
    return digitsSum


def isSmithnumber(number, primes):
    primeFactors = []
    index = 0
    digitSum = sumOfDigits(number)

    while number > 1:
        if number % primes[index] == 0:
            primeFactors.append(primes[index])
            number = number // primes[index]
        else:
            index += 1

    if sum(primeFactors) == digitSum:
        return True
    return False


def fun_nth_smithnumber(n):
    smithNumbers = []
    start = 4
    while(len(smithNumbers) - 1 < n):
        if isPrime(start):
            start = start + 1
        else:
            primes = listOfPrimes((start // 2) + 1)
            if isSmithnumber(start, primes):
                smithNumbers.append(start)
            start += 1
    return smithNumbers[n]


print(fun_nth_smithnumber(0))
print(fun_nth_smithnumber(1))
print(fun_nth_smithnumber(2))
