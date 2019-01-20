# Levi VonBank

def main():
    
    # Initializes an empty list for user input
    values = []
    
    # loop that reads input and appends it to list values
    print('Please enter values, "Enter" to quit:')
    userInput = input("")
    while userInput != "":
        values.append(float(userInput))
        userInput = input("")
    
    # Prints the list with the minimum value eliminated
    print(sumWithoutSmallest(values))

## Removes the minimum value from a list
# @parm values takes a list of values
# @return the difference (smallest removed)
# 
def sumWithoutSmallest(values):
    if values != []:
        smallest = values[0]
        listSum = 0
        for i in range(len(values)):
            if values[i] < smallest:
                smallest = values[i]
            listSum += values[i]
        return listSum - smallest
    return 0

main()