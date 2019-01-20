# Levi VonBank

from math import sqrt

# This prompts the user to put in the lengths of the sides of a rectangle
userInput1 = input("Please input the longest side: ")
longSide = float(userInput1)

userInput2 = input("Please input the shortest side: ")
shortSide = float(userInput2)

# Prints the area, perimeter, and length of the diagnal
print()
print("The area is: ", longSide * shortSide)
print("The perimeter: ", (2 * (longSide + shortSide)))
print("The length of the diagnal is: ", sqrt(longSide ** 2 + shortSide ** 2))