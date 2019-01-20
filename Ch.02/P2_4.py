# Levi VonBank

# Prompts the user for two integers and then prints
number1 = int(input("Enter the first integer: "))
number2 = int(input("Enter the second integer: "))


numbersSum = number1 + number2           # Sum 
numbersDifference = number1 - number2    # difference
numbersProduct = number1 * number2       # product
numbersAverage = (number1 + number2) / 2 # average
numbersDistance = abs(number1 - number2) # distance
numbersMax = max(number1, number2)       # max
numbersMin = min(number1, number2)       # min

print()
print("The sum is: %d" % numbersSum)
print("The difference is: %d" % numbersDifference)
print("The product is: %d " % numbersProduct)
print("The average is: %d" % numbersAverage)
print("The distance is: %d" % numbersDistance)
print("The maximum is: %d" % numbersMax)
print("The minimum is: %d" % numbersMin)