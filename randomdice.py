from random import randrange as r

def RandomDice(dice, mode="sum"):
    """
        This function rolls a dice_num of 'dice' between min and max
        prints each die rolled and returns the result
    """

    dice = dice.split("d")
    dice_num = int(dice[0])
    min = 1
    max = int(dice[1])

    result = 0
    dice = []

    if mode == "sum":
        for roll in range(dice_num):
            baseDie = r(min, max+1)
            print(baseDie, end=" ")
            result += baseDie 
        print(f"Result is : {result}")

    elif mode == "dl1":
        for roll in range(dice_num):
            die = r(min, max+1)
            dice.append(die)
            print(die, end=" ")

        print()
        dice = sorted(dice, reverse=True)
        
        print(dice)
        dice.pop()

        die1, die2, die3 = dice
        print(die1, die2, die3)


        result = sum(dice)
        print(f"Result is : {result}")
    elif mode == "kh1":
        for roll in range(dice_num):
            die = r(min, max+1)
            dice.append(die)
            print(die, end=" ")

        print()
        dice = sorted(dice)
        
        print(dice)
        dice = dice.pop()

        result = dice
        print(f"Result is : {result}")
    elif mode == "kl1":
        for roll in range(dice_num):
            die = r(min, max+1)
            dice.append(die)
            print(die, end=" ")

        print()
        dice = sorted(dice, reverse=True)
        
        print(dice)
        dice = dice.pop()

        result = dice
        print(f"Result is : {result}")

    return result
