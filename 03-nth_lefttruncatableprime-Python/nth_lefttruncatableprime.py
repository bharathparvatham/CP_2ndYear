# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math


def sumOfDigits(number):
    if number < 9:
        return 1
    count = 0
    while number > 0:
        count += 1
        number = number // 10
    return count


def isPrime(number):
    if number < 2:
        return False

    for num in range(2, math.floor(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def fun_nth_lefttruncatableprime(n):
    count = 0
    leftTruncatbalePrime = 2
    start = 3
    while (count < n):
        if isPrime(start):
            if start < 9:
                count += 1
                leftTruncatbalePrime = start
            elif sumOfDigits(start) - sumOfDigits(start % (10 ** (sumOfDigits(start) - 1))) != 1:
                start += 1
                continue
            elif isPrime(start % (10 ** (sumOfDigits(start) - 1))):
                count += 1
                leftTruncatbalePrime = start
        start += 1
    return leftTruncatbalePrime


print(fun_nth_lefttruncatableprime(10))
print(fun_nth_lefttruncatableprime(15))
print(fun_nth_lefttruncatableprime(16))
print(fun_nth_lefttruncatableprime(17))
print(fun_nth_lefttruncatableprime(18))
print(fun_nth_lefttruncatableprime(19))
print(fun_nth_lefttruncatableprime(20))
print(fun_nth_lefttruncatableprime(25))
