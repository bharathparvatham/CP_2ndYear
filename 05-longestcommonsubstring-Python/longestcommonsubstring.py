# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    if len(s1) < len(s2):
        smaller = s1
        bigger = s2
    else:
        smaller = s2
        bigger = s1

    result = ""
    maxSubString = ""

    for letter in smaller:
        if result + letter in bigger:
            result += letter
        elif letter in bigger:
            if len(maxSubString) <= len(result):
                maxSubString = result
            result = letter
        else:
            if len(maxSubString) <= len(result):
                maxSubString = result
            result = ""
    if len(maxSubString) <= len(result):
        maxSubString = result

    return maxSubString
