# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
    # Your code goes here
    sumCol = None
    sumRow = None

    for col in range(len(a)):
        colSum = 0
        for row in a:
            colSum += row[col]
            rowSum = sum(row)
            if sumRow is None:
                sumRow = rowSum
            elif sumRow != rowSum:
                return False

        if sumCol is None:
            sumCol = colSum
        elif sumCol != colSum:
            return False

        if sumRow != sumCol:
            return False

    diagonal1 = 0
    for i in range(len(a)):
        diagonal1 += a[i][i]

    if diagonal1 != sumCol != sumRow:
        return False

    diagonal2 = 0
    index = len(a) - 1
    for i in range(len(a)):
        diagonal2 += a[i][index]
        index -= 1

    if diagonal2 != sumRow != sumCol != diagonal1:
        return False

    return True
