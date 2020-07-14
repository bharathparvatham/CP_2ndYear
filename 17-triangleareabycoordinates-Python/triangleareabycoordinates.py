# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
    # your code goes here
    s1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    s2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
    s3 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5

    s = (s1 + s2 + s3) / 2

    if (s - s1) > 0 and (s - s2) > 0 and (s - s3) > 0:
        return (s * (s - s1) * (s - s2) * (s - s3)) ** 0.5
    return 0
