# Levi VonBank

from math import sqrt

# Initializes variables
total = 0.0
devTotal = 0
count = 0

# Priming read
userInput = float(input("Enter a value or -1 to finish: "))

# Enters a loop to determine the average and standard deviation
while userInput >= 0.0:
    total = total + userInput
    devTotal = devTotal + userInput**2
    count = count + 1
    userInput = float(input("Enter a value or -1 to finish: "))

# Makes sure the count is not zero
if count > 0 :
    average = total / count
else :
    average = 0.0

# Solves for standard deviation
partOne = devTotal
partTwo = ((1/count) * ((total)**2))
partThree = count - 1
partFour = (partOne - partTwo) / partThree
stanDev = sqrt(partFour)

print()
print("The count of the values is:", count)
print("The average of the values is:", average)
print("The standard deviation of the values is:", stanDev)