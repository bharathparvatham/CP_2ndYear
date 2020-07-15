# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    # your code goes here
    previousDigit = -2
    n = abs(n)
    while n > 0:
        if n % 10 == previousDigit:
            return True
        else:
            previousDigit = n % 10
            n = n // 10
    return False
