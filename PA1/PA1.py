# Levi VonBank

# Imports the command to exit program
from sys import exit

# Obtains an 8-digit credit card number from the user
usersInput = input("Enter an 8-digit credit card number: ")

# Removes spaces and dashes if entered
creditCardNumber = ""
for char in usersInput:
    if char != " " and char != "-":
        creditCardNumber = creditCardNumber + char

# Validates if the credit card number is the correct length and digits
if not (creditCardNumber.isdigit()):  # Validates digits
    exit("You can only enter digits")
if not (len(creditCardNumber) == 8):  # Validates length
    exit("You must enter at least 8 digits total")
        
# Initializes variables for first calculation
firstConcatenate = ""
i = len(creditCardNumber) -1

# This retrieves the righter most number and moves to the left by multiples of two
while i < len(creditCardNumber) and i >= 0:
        number = creditCardNumber[i]
        firstConcatenate = firstConcatenate + number
        i = i -2
        
# Removes the check digit from the calculation (this simplifies checking)
firstConcatenate = str(int(firstConcatenate) % 1000)

# Initializes variables for adding the firstConcatenate together 
i = 0
total1 = 0

# Adds up the numbers in the firstConcatenate
while i < len(firstConcatenate):
    number = firstConcatenate[i]
    total1 = total1 + int(number)
    i = i + 1

# Initializes variables for The second calculation
secondConcatenate = ""
i = len(creditCardNumber) -2

# This retrieves the second to last number & moves to the left by multiples of two
while i < len(creditCardNumber) and i >= 0:
        number = creditCardNumber[i]
        number = int(number) * 2
        secondConcatenate = secondConcatenate + str(number)
        i = i -2

# Initializes variables for adding the secondConcatenate together
i = 0
total2 = 0

# Adds up the numbers in the secondConcatenate (each individual character)
while i < len(secondConcatenate):
    number = secondConcatenate[i]
    total2 = total2 + int(number)
    i = i + 1

# Adds the final totals together (Produced from calculating the two concatenate)
finalTotal = total1 + total2

# Initializes variables for finding the checkDigit
nonCheck = (finalTotal) * 9
checkDigit = nonCheck % 10

# Retrieves the check digit to compare to users entry for validation
lastChar = len(creditCardNumber) -1
lastDigit = int(creditCardNumber[lastChar])

# Determines if the credit card is a valid one or what the checkDigit should be
if lastDigit == checkDigit:  # Checks to see if the card numbers valid
    string1 = ""
    string2 = ""
else:                        # Determines what the checkDigit should be if invalid
    string1 = "not "
    string2 = "The check digit should be: %s" % checkDigit
    
print("The number is %svalid. %s" % (string1, string2))
