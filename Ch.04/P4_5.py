# Levi VonBank

# Initializes variables
total = 0.0
count = 0

# Priming read
inputStr = input("Enter a value or Q to quit: ")

# Initializes the largest and smallest variables
largest = float(inputStr)
smallest = float(inputStr)

# Enters a loop to determine the largest, smallest, and average
while inputStr.upper() != "Q" :
    value = float(inputStr)
    total = total + value
    count = count + 1
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value
    inputStr = input("Enter a value or Q to quit: ")
    
# Makes sure the count is not zero
if count > 0 :
    average = total / count
else :
    average = 0.0

# Calculates the range
dataRange = largest - smallest

print()
print("The average of the values is:", average)
print("The smallest of the values is:", smallest)
print("The largest of the values is:", largest)
print("The range of the values is:", dataRange)