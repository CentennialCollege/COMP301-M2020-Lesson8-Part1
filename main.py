from random import Random
from square import Square as sqr
#from maximum import Maximum as max

from randomdice import RandomDice

squareOf5 = sqr(5)

print("Square of 5 is " + str(squareOf5))

print(sqr)

squareOf5 = sqr

print(squareOf5(5))

values = [10, 11, 5]

result = max(values[0], values[1], values[2])

print(f"The Maximum value (of an int) is: {result}")


values = [10.7, 11.345, 5.123456789]

result = max(values[0], values[1], values[2])

print(f"The Maximum value (of a float) is: {result}")


values = ["Toronto", "Mississauga", "Oshawa"]

result = max(values[0], values[1], values[2])

print(f"The Maximum value (of a string) is: {result}")

diceResult = RandomDice(1, 6, 4)

diceResult = RandomDice(1, 6, 4, "dl1")

diceResult = RandomDice(1, 20, 2, "kh1")