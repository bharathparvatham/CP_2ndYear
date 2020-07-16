# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def happyNumber(number):
    while (n > 9):
        sumOfSquaresOfDigits = 0
        while (n > 0):
            sumOfSquaresOfDigits += (n % 10) ** 2
            n = n // 10
        sumOfSquaresOfDigits = n
    if n == 1 or n == 7:
        return True
    return False


def fun_nth_happy_number(n):
    happyNumberList = [1, 7]
    if n > len(happyNumberList) - 1:
        number = 10
        while n != len(happyNumberList) - 1:
            if happyNumber(number):
                happyNumberList.append(number)
            number += 1

    return happyNumberList[n]
