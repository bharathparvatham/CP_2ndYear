# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidyNumber(number):
    lastDigit = number % 10
    number = number // 10

    while number > 0:
        digit = number % 10
        if lastDigit >= digit:
            number = number // 10
        else:
            return False
    return True


def fun_nth_tidynumber(n):
    count = 0
    tidyNumber = 1
    start = 2

    while count < n:
        if start < 10:
            count += 1
            tidyNumber = start
            start += 1
        else:
            if isTidyNumber(start):
                count += 1
                tidyNumber = start
            start += 1

    return tidyNumber
