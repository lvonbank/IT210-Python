# Levi VonBank

# Write a program that reads in a string and prints whether it

userInput = str(input("Enter a string: "))

# contains only letters.
if userInput.isalpha():
    print("Contains only letters.")

# contains only uppercase letters.
if userInput.isupper():
    print("Contains only uppercase letters.")

# contains only lowercase letters.
if userInput.islower():
    print("Contains only lowercase letters.")

# contains only digits.
if userInput.isdigit():
    print("Contains only digits.")

# contains only letters and digits.
if userInput.isalnum():
    print("Contains only letters and digits.")

# starts with an uppercase letter.
if userInput[0].isupper():
    print("Starts with an uppercase letter.")

# ends with a period.
if userInput.endswith("."):
    print("Ends with a period")