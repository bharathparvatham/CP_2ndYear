# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….
def reverse(number):
    number = str(number)
    result = number[:: -1]
    return int(result)


def isPalindrome(number):
    number = str(number)
    return number == number[:: -1]


def isLychrelNumber(number):

    for i in range(25):
        number += reverse(number)
        if isPalindrome(number):
            return False
    return True


def nthlychrelnumbers(n):
    # your code goes here
    count = 1
    lychrelNumber = 196

    start = 197

    while count < n:
        if isLychrelNumber(start):
            count += 1
            lychrelNumber = start
        start += 1

    return lychrelNumber


for i in range(1, 5):
    print(nthlychrelnumbers(i))
