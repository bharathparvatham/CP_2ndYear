# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


import math


def countOfDigits(number):
    if number < 9:
        return 1
    count = 0
    while(number > 0):
        count += 1
        number = number // 10
    return count


def isKaprekarNumber(number):
    if number < 0:
        return False

    sqroot = number ** 2
    count = countOfDigits(sqroot)
    rightCount = 1

    while rightCount < count:
        if (sqroot % (10 ** rightCount)) + (sqroot // (10 ** rightCount)) == (10 ** rightCount):
            return False
        if (sqroot % (10 ** rightCount)) + (sqroot // (10 ** rightCount)) == number:
            return True
        rightCount += 1
    return False


def fun_nearestkaprekarnumber(n):
    count = 1
    while True:
        if isKaprekarNumber(n):
            return n
        else:
            if isKaprekarNumber(n - count):
                return (n - count)
            elif isKaprekarNumber(n + count):
                return (n + count)
        count += 1


print(fun_nearestkaprekarnumber(49))
print(fun_nearestkaprekarnumber(51))
print(fun_nearestkaprekarnumber(50))
print(fun_nearestkaprekarnumber(102))
print(fun_nearestkaprekarnumber(765))
print(fun_nearestkaprekarnumber(3861))
