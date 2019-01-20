# Levi VonBank

## Reads a floating point number and prints “zero” if the number is zero. 
# Otherwise “positive” or “negative”. “small” if it is less than 1, 
# or “large” if it exceeds 1,000,000.

userInput = float(input("Enter a floating-point number: "))

if userInput == 0:
    print("It's zero")

elif userInput > 0:
    print("It's positive")

else:
    print("It's negative")

if userInput < 1:
    print("and small")

elif userInput > 1000000:
    print("and large")