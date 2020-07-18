# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def findzerowithbisection(x, epsilon):
    # epsilon and step are initialized
    # don't change these values
    # epsilon
    # your code starts here

    start = 1
    end = x
    mid = (start + end) / 2
    while(abs(start - end) > epsilon):
        mid = (start + end) / 2
        if (x - (start ** 2)) == 0:
            return start
        elif (x - (mid ** 2)) == 0:
            return mid
        elif (x - (end ** 2)) == 0:
            return end
        elif ((x - (start ** 2)) < 0 and (x - (mid ** 2)) > 0) or ((x - (start ** 2)) > 0 and (x - (mid ** 2)) < 0):
            end = mid
        else:
            start = mid
    return mid
