# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2

import math


def isPrime(number):
    for index in range(2, math.floor(number ** 0.5) + 1):
        if number % index == 0:
            return False
    return True


def primesInRange(start, end):
    primes = []
    for index in range(start, end + 1):
        if isPrime(index):
            primes.append(index)
    return primes


def isPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False


def fun_nth_palindromic_prime(n):
    palindromicPrimes = [2, 3, 7, 11]

    if n < len(palindromicPrimes) - 1:
        return palindromicPrimes[n]

    else:
        start = 13
        while n > len(palindromicPrimes) - 1:
            primes = primesInRange(start, start + 100)
            for prime in primes:
                if isPalindrome(prime):
                    palindromicPrimes.append(prime)
                    if n == len(palindromicPrimes) - 1:
                        break
        return palindromicPrimes[n]


print(fun_nth_palindromic_prime(10))
