# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
import math


def isPrime(number):
    if number == 0 or number == 1:
        return False

    for num in range(2, math.floor(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def digitsCount(number):
    if number < 10:
        return 1

    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def rightRotate(number):
    if number < 10:
        return []

    rotatedNumber = []
    count = digitsCount(number)

    rightRotate = (number % 10) * (10 ** (count - 1)) + (number // 10)

    while(rightRotate != number):
        rotatedNumber.append(rightRotate)
        rightRotate = (rightRotate % 10) * \
            (10 ** (count - 1)) + (rightRotate // 10)

    return rotatedNumber


def nthcircularprime(n):
    # Your code goes here
    count = 1
    circularPrime = 2
    start = 3

    while count < n:
        if isPrime(start):
            flag = True
            if start > 10:
                rightrotate = rightRotate(start)
                if rightrotate != []:
                    for rotatedNumber in rightrotate:
                        if isPrime(rotatedNumber) == False:
                            flag = False
                            break
                else:
                    flag = False
            if flag:
                count += 1
                circularPrime = start
        start += 1
    return circularPrime
