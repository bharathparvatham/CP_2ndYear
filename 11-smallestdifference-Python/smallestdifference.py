# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
    # Your code goes here
    if len(a) == 0:
        return -1
    if len(a) == 1:
        return a[0]
    a.sort()
    minimum = abs(a[1] - a[0])
    for index in range(1, len(a) - 1):
        if minimum > abs(a[index + 1] - a[index]):
            minimum = abs(a[index + 1] - a[index])
    return minimum
