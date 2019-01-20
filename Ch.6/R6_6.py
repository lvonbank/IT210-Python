# Levi VonBank

def main():
    
    # Initializes an empty list for user input
    lis = []
    
    # loop that reads input and appends it
    print('Please enter input, "Enter" to quit:')
    userInput = input("")
    while userInput != "":
        lis.append(userInput)
        userInput = input("")
    
    # Prints a tuple with the minimum & maximum values
    print(minMax(lis))

## Computes the minimum and maximum value in a list
# @lis takes a list
# @return the minimum and maximum as a tuple
# 
def minMax(lis):
    if lis != []:
        largest = lis[0]
        smallest = lis[0]
        for i in range(1,len(lis)):
            if lis[i] > largest:
                largest = lis[i]
            if lis[i] < smallest:
                smallest = lis[i]
        return (smallest, largest)
    return ()

main()