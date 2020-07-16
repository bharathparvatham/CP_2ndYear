# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list
# is sorted (either smallest-first or largest-first) and False otherwise. Your function
# must only consider each value in the list once (so, in terms of big-oh, which we will
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort
# the list.

def lessThan(arr):
    for index in range(len(arr) - 1):
        if arr[index] > arr[index + 1]:
            return False
    return True


def greaterThan(arr):
    for index in range(len(arr) - 1):
        if arr[index] < arr[index + 1]:
            return False
    return True


def issorted(a):
    # your code goes here
    if len(a) == 0 or len(a) == 1:
        return True
    index = 0

    while(index + 1 < len(a)):
        if a[index] == a[index + 1]:
            index += 1
        elif a[index] < a[index + 1]:
            return lessThan(a[index:])
        else:
            return greaterThan(a[index:])
    return True
