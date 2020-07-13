from random import randrange as r

def RandomDice(min, max, dice_num, mode="sum"):
    """
        This function rolls a dice_num of 'dice' between min and max
        prints each die rolled and returns the result
    """

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

    return result
