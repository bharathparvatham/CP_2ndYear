# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isUgly(number):

    while number > 1:
        if number % 2 == 0:
            number = number // 2
        elif number % 3 == 0:
            number = number // 3
        elif number % 5 == 0:
            number = number // 5
        else:
            return False
    return True


def fun_nth_uglynumber(n):
    count = 0
    uglyNumber = 1
    start = 2

    while count < n:
        if isUgly(start):
            count += 1
            uglyNumber = start
        start += 1

    return uglyNumber
