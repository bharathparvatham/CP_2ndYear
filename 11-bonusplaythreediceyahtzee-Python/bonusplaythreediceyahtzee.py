# bonusPlayThreeDiceYahtzee(dice) [5pts]
# In this exercise, we will write a simplified form of the dice game Yahtzee. In this version, the
# goal is to get 3 matching dice, and if you can't do that, then you hope to at least get 2
# matching dice. The game is played like so:
# Roll 3 dice.
# If you do not have 3 matching dice:
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# Otherwise, if you have no matching dice, keep the highest die and roll two dice to replace the
# other two dice.
# Repeat step 2 one more time.
# Finally, compute your score like so:
# If you have 3 matching dice, your score is 20 + the sum of the matching dice.
# So if you have 4-4-4, your score is 20+4+4+4, or 32.
# If you only have 2 matching dice, your score is 10 + the sum of the matching dice.
# So if you have 4-4-3, your score is 10+4+4, or 18.
# If you have no matching dice, your score is the highest die.
# So if you have 4-3-2, your score is just 4.
# Our goal is to write some Python code that plays this game. It's a large task, so we will use
# top-down design and break it up into smaller, more manageable pieces. So we'll first write some
# helper functions that do part of the work, and then those helper functions will make our final
# function much easier to write.

# Also note: we will represent a hand of 3 dice as a single 3-digit integer. So the hand 4-3-2 will
# be represented by the integer 432. With that, let's start writing some code. Be sure to write
# your functions in the same order as given here, since later functions will make use of earlier
# ones!

# we've made it to the last function: bonusPlayThreeDiceYahtzee(dice), the function that actually earns
# the 2.5 bonus points! This function takes one value, the dice with all the rolls for a game of 3-Dice
# Yahtzee. The function plays the game -- it does step1 and gets the first 3 dice (from the right), then it
# does step2 twice (by calling playStep2, which you already wrote), and then it computes the score (by
# calling score, which you already wrote). The function should return two values -- the resulting hand
# and the score for that hand. For example:
# assert(bonusPlayThreeDiceYahtzee(2312413) == (432, 4))
# assert(bonusPlayThreeDiceYahtzee(2315413) == (532, 5))
# assert(bonusPlayThreeDiceYahtzee(2345413) == (443, 18))
# assert(bonusPlayThreeDiceYahtzee(2633413) == (633, 16))
# assert(bonusPlayThreeDiceYahtzee(2333413) == (333, 29))
# assert(bonusPlayThreeDiceYahtzee(2333555) == (555, 35))

def score(dice):
    dice = str(dice)
    if dice[0] == dice[1] == dice[2]:
        return int(dice), 20 + (int(dice[0]) * 3)
    elif dice[0] == dice[1]:
        return int(dice), 10 + (int(dice[0]) * 2)
    elif dice[1] == dice[2]:
        return int(dice), 10 + (int(dice[1]) * 2)
    elif dice[2] == dice[0]:
        return int(dice), 10 + (int(dice[2]) * 2)
    else:
        return int(dice), int(max(dice[0], dice[1], dice[2]))


def step2(leftOverDices, presentDice):
    presentDice = str(presentDice)
    leftOverDices = str(leftOverDices)
    if presentDice[0] == presentDice[1] == presentDice[2]:
        return score(int(presentDice))
    elif presentDice[0] == presentDice[1]:
        presentDice = presentDice[0:2]
        maximum = "-1"
        for i in leftOverDices:
            if i > maximum:
                maximum = i
        if presentDice[0] > maximum:
            presentDice += maximum
        else:
            presentDice = maximum + presentDice
        return score(int(presentDice))
    elif presentDice[1] == presentDice[2]:
        presentDice = presentDice[1:3]
        maximum = "-1"
        for i in leftOverDices:
            if i > maximum:
                maximum = i
        if presentDice[0] > maximum:
            presentDice += maximum
        else:
            presentDice = maximum + presentDice
        return score(int(presentDice))
    elif presentDice[0] == presentDice[2]:
        presentDice = presentDice[0] + presentDice[2]
        maximum = "-1"
        for i in leftOverDices:
            if i > maximum:
                maximum = i
        if presentDice[0] > maximum:
            presentDice += maximum
        else:
            presentDice = maximum + presentDice
        return score(int(presentDice))
    else:
        presentDiceList = [presentDice[0], presentDice[1], presentDice[2]]
        presentDiceList.sort()

        if len(leftOverDices > 2):
            temp = [presentDiceList[-1], leftOverDices[-1], leftOverDices[-2]]
            temp.sort(reverse=True)
            presentDice = "".join(temp)
            return step2(int(leftOverDices[:len(leftOverDices) - 2]), int(presentDice))
        elif len(leftOverDices) == 2:
            temp = [presentDiceList[-1], leftOverDices[-1], leftOverDices[-2]]
            temp.sort(reverse=True)
            presentDice = "".join(temp)
            return score(int(presentDice))
        elif len(leftOverDices) == 1:
            temp = [presentDiceList[-1],
                    presentDiceList[-2], leftOverDices[-1]]
            temp.sort(reverse=True)
            presentDice = "".join(temp)
            return step2(int(leftOverDices[:len(leftOverDices) - 1]), int(presentDice))
        elif len(leftOverDices) == 0:
            return score(int(presentDice))


def step1(dice):
    leftOverDices = dice // 1000
    presentDice = dice % 1000
    if leftOverDices > 0:
        step2(leftOverDices, presentDice)
    else:
        return score(presentDice)


def bonusplaythreediceyahtzee(dice):
    # Your code goes here
    return step1(dice)
