# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).
import math


def primeInRange(start, end):
    primeNumbers = []
    number = start
    while(number <= end):
        flag = True
        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                flag = False
                break
        if flag:
            primeNumbers.append(number)
        number += 1
    return primeNumbers


def happyNumber(n):
    if n <= 0:
        return False
    if n == 1 or n == 7:
        return True
    while(n > 9):
        sumOfSquaresOfDigits = 0
        while(n > 0):
            sumOfSquaresOfDigits += (n % 10) ** 2
            n = n // 10
        n = sumOfSquaresOfDigits
    if n == 1 or n == 7:
        return True
    return False


def fun_nth_happy_prime(n):
    if n == 0:
        return 7
    start = 7
    end = n + 10
    primeNumberList = primeInRange(start, end)

    happyNumbers = [7]

    while n > len(happyNumbers) - 1:
        for prime in primeNumberList:
            if happyNumber(prime):
                happyNumbers.append(prime)
        if n > len(happyNumbers) - 1:
            start = end + 1
            end = start + 10
            primeNumberList = primeInRange(start, end)
    return happyNumbers[n]
