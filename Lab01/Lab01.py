# Levi VonBank

# First programming assignment - convert pound to other units of weight

# Get input in pounds
# Note that the input function always give a string

lbsStr = input("Enter the number of pounds: ")
lbs = float(lbsStr) # Convert the string to a float

# compute other units of weight
ozs = lbs * 16
tons = lbs / 2000.
stones = lbs * 0.0714285714286
kilograms = lbs * 0.45359237

#output the results of the calculation
print() # Prints a blank line
print(lbs, "pounds is the same as: ")
print(ozs, "ounces")
print(tons, "tons")
print(stones, "stones")
print(kilograms, "kilograms")