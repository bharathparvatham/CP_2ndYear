# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    if lengthS1 < lengthS2:
        return s1
    index = 0
    while (index + lengthS2 - 1 < lengthS1):
        if s1[index: index + lengthS2] == s3:
            result = s1[0: index] + s3 + s1[index + lengthS2:]
            return fun_replace(result, s2, s3)
        index += 1
    return s1
