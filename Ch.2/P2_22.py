# Levi VonBank

## Initializes a string variable and prints the first three characters
# followed by three periods

userInput = str(input("Enter a string: "))

last = len(userInput) - 1

firstThree = userInput[0] + userInput[1] + userInput[2]
LastThree = userInput[last-2] + userInput[last-1] + userInput[last]
middle = "..."

print(firstThree + middle + LastThree)