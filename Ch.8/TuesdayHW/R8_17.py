# Levi VonBank

# Imports ascii_letters
from string import ascii_letters

def main():
    str1 = input("Enter a first string: ")
    str2 = input("Enter a second string: ")
    
    printout(lettersIn(str1, str2))
    printout(lettersNotIn(str1, str2))
    printout(notLetter(str1, str2))

## Provides a set with letters contained in both strings
# @parm str1 & str2 takes strings
# @return a set containing letters in both strings
def lettersIn(str1, str2):
    mergedStrings = set(str1 + str2)
    letters = set(ascii_letters)
    return letters.intersection(mergedStrings)

## Provides a set with letters contained in neither strings
# @parm str1 & str2 takes strings
# @return a set containing letters in neither strings
def lettersNotIn(str1, str2):
    mergedStrings = set(str1 + str2)
    letters = set(ascii_letters)
    return letters.difference(mergedStrings)

## Provides a set with none letters in the two strings
# @parm str1 & str2 takes strings
# @return a set containing none letters in the two strings
def notLetter(str1, str2):
    notLet = set()
    mergedStrings = set(str1 + str2)
    letters = set(ascii_letters)
    for char in mergedStrings:
        if char not in letters:
            notLet.add(char)
    return notLet

## Formats and prints any provided set
# @parm takes a set and prints it
def printout(setinput):
    print('|', end="")
    for char in sorted(setinput):
        print(char, end="")
    print('|')

main()