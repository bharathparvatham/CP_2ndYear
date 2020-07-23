# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After
# some thought, we see that no matter what number we start with, when we keep replacing
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n).
# And that's top-down design! Here we go....
# Note: the autograder will grade each of the following functions, so they are required.
# However, they also are here specifically because they are just the right helper
# functions to make nthHappyNumber(n) easier to write!
import math


def isPrime(number):
    if number < 2:
        return False
    for num in range(2, math.floor(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True


def sumOfDigits(number):
    if number < 9:
        return number ** 2

    result = 0

    while(number > 0):
        result = result + ((number % 10) ** 2)
        number = number // 10

    return result


def isHappy(number):
    if number < 10:
        if number == 1:
            return True
        else:
            return False

    while(number >= 10):
        number = sumOfDigits(number)
        if number < 10:
            if number == 1:
                return True
            else:
                return False


def ishappyprimenumber(n):
    # Your code goes here
    if n < 0:
        return False

    if isPrime(n) == False:
        return False

    if (n < 10):
        if n == 1:
            return True
        else:
            return False

    if isHappy(n):
        return True

    return False
