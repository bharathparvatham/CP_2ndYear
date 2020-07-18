# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that
# any values that would otherwise produce a consecutive run of k elements are not present.
# For example:
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3])
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3])
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
    # Your code goes here
    count = 1
    length = len(L)
    i = 0
    while (i < length - 1):
        if L[i] == L[i + 1]:
            count += 1
            if count == k:
                del L[i]
                count = 1
                i -= 1
                length -= 1
        else:
            count = 1
        i += 1
    return L
