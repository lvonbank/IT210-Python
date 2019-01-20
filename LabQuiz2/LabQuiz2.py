# Levi VonBank

from string import ascii_letters, ascii_lowercase, ascii_uppercase
from string import digits, hexdigits, punctuation

# Initializes input from user
userInput = input("Enter a string: ")

# Creates a loop for more userInput
while userInput != "":
    
    # Initializes variables 
    length = len(userInput)
    backwards = userInput[::-1]
    noPunct = ""
    lower = ""
    hexDig = 0
    
    # Checks if users string contains appropriate content for each case
    for char in userInput:
        if char not in punctuation:
            noPunct += char
        if char in ascii_lowercase:
            lower += char
        if char in hexdigits:
            hexDig += 1
    
    # Printsthe final results
    print("The length of is:", length)
    print(backwards)
    print(noPunct)
    print(lower)
    print("Total hexdigits:", hexDig)


    userInput = input("Enter a string: ")

print("Done.")