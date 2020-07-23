# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math


def countOfDigits(number):
    count = 0
    if number < 9:
        return 1
    while(number > 0):
        count += 1
        number = number // 10
    return count


def isKaprekarNumber(number):
    sqroot = number ** 2
    count = countOfDigits(sqroot)
    rightCount = 1
    while rightCount < count:
        if (sqroot % (10 ** rightCount)) + (sqroot // (10 ** rightCount)) == int(10 ** rightCount):
            return False
        if (sqroot % (10 ** rightCount)) + (sqroot // (10 ** rightCount)) == number:
            return True
        rightCount += 1
    return False


def fun_nth_kaprekarnumber(n):
    count = 0
    kaprekarnumber = 1
    start = 1
    while(count < n):
        if isKaprekarNumber(start):
            count += 1
            kaprekarnumber = start
        start += 1
    return kaprekarnumber
