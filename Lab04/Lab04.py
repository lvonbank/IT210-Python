# Levi VonBank
# Group Members: Scott Fleming and Dura Keonangphane

## 
# Write a program that reads an integer and displays an asterisks filled 
# diamond from a given side length.
#

# Obtains a side length from the user
side = int(input("Please input side length of diamond: "))

if side >= 0:
    for index in range(side - 1):
        print((side - index - 1) * ' ' + (2 * index + 1) * '*')
    for index in range(side - 1, -1, -1):
        print((side - index - 1) * ' ' + (2 * index +1) * '*')
