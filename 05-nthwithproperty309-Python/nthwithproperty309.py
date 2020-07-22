# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.
def hasPropert309(number):
    string = str(number ** 5)

    for digit in range(0, 10):
        if str(digit) not in string:
            return False
    return True


def nthwithproperty309(n):
    # Your code goes here
    start = 309
    numbersWithProperty = []

    while(len(numbersWithProperty) - 1 < n):
        if hasPropert309(start):
            numbersWithProperty.append(start)
        start += 1
    return numbersWithProperty[n]


print(nthwithproperty309(0))
print(nthwithproperty309(1))
print(nthwithproperty309(2))
print(nthwithproperty309(3))
print(nthwithproperty309(4))
print(nthwithproperty309(5))
print(nthwithproperty309(6))
print(nthwithproperty309(100))
print(nthwithproperty309(1000))
