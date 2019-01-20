# Levi VonBank

from string import ascii_uppercase

def main():
    # Obtains users input
    str1 = input("Enter a first string: ")
    str2 = input("Enter a second string: ")

    # Creates a set of each string
    str1 = set(str1.upper())
    str2 = set(str2.upper())
    
    # Characters that occurs in both
    printout(str1.intersection(str2))
    
    # Characters that occurs in str1
    printout(str1.difference(str2))
    
    # Characters that occurs in str2
    printout(str2.difference(str1))

    # Letters that don't occurs in either
    mergedStr = str1.union(str2)
    char = set(ascii_uppercase)
    printout(char.difference(mergedStr))

## Formats and prints any provided set
# @parm takes a set and prints it
def printout(setinput):
    for char in sorted(setinput):
        print(char, end="")
    print()

main()