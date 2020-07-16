from random import randrange as r

def RandomDice(dice, mode="sum"):
    """
        This function rolls a dice_num of 'dice' between min and max
        prints each die rolled and returns the result
    """

    #splits the dice argument into two parts dice[0] and dice[1]
    dice = dice.split("d")
    dice_num = int(dice[0]) # how many dice
    min = 1
    max = int(dice[1]) # dice type

    result = 0
    dice = []

    print("Mode: " + mode)
    print("Rolls: ", end="")

    #roll
    for roll in range(dice_num):
        baseDie = r(min, max+1)
        if mode == "sum":
            result += baseDie 
        else:
            dice.append(baseDie)
        print(baseDie, end=" ")

    if(mode != "sum"):
        dice = sorted(dice) if mode == "kh1" else sorted(dice, reverse=True) #sort
        
        if mode == "dl1": #drop a die
            dice.pop()
        result = sum(dice) if mode == "dl1" else dice.pop()

    print(f"\nResult is : {result} \n")

    return result
