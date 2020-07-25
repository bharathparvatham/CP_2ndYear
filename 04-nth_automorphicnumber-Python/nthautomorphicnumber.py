# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.

def isAutomorphic(number, square):
    while number > 0:
        if (number % 10) == (square % 10):
            number = number // 10
            square = square // 10
        else:
            return False
    return True


def nthautomorphicnumbers(n):
    # Your code goes here
    count = 1
    automorphicNumber = 0
    start = 1

    while count < n:
        squareOfNum = start ** 2

        if isAutomorphic(start, squareOfNum):
            count += 1
            automorphicNumber = start

        start += 1
    return automorphicNumber
