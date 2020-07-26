# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def permutationsHelper(string):
    if len(string) == 1:
        return string
    else:
        permutation = []
        for index in range(len(string)):
            result = permutationsHelper(
                string[0: index] + string[index + 1:])
            if type(result) is str:
                permutation.append((string[index], ) + (result, ))
            else:
                for i in range(len(result)):
                    permutation.append((string[index], ) + result[i])
        return permutation


def getallpermutations(x):
    # Your code goes here
    if x == "":
        return ""
    return permutationsHelper(x)
