# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    dictionary = {}

    for chr in s:
        chrCount = s.count(chr)
        if chrCount in dictionary.keys():
            if chr not in dictionary[chrCount]:
                dictionary[chrCount].append(chr)
        else:
            dictionary[chrCount] = [chr]

    resultArray = []
    keys = list(dictionary.keys())
    keys.sort(reverse=True)
    for key in keys:
        resultArray.extend(dictionary[key])

    return resultArray[n - 1]
