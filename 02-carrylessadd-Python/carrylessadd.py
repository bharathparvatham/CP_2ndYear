# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

def listToNumber(List):
    result = 0
    for index in range(len(List) - 1, -1, -1):
        result = (result * 10) + List[index]
    return result


def helper(x, y, result):
    add = 0
    if x > 9:
        add += (x % 10)
        x = x // 10
    elif 0 <= x <= 9:
        add += x
        x = x // 10

    if y > 9:
        add += (y % 10)
        y = y // 10
    elif 0 <= y <= 9:
        add += y
        y = y // 10

    result.append(add % 10)

    if x != 0 or y != 0:
        return helper(x, y, result)

    return result


def fun_carrylessadd(x, y):
    return listToNumber(helper(x, y, []))
