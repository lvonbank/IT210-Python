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
    
    # Prints the list with the minimum value eliminated
    print(removeMin(lis))

## Removes the minimum value from a list
# @parm lis takes a list
# @return provides a list with the minimum removed
# 
def removeMin(lis):
    smallPos = 0
    if lis != []:
        for i in range(1, len(lis)):
            if lis[i] < lis[smallPos]:
                smallPos = i
        lis = lis[:smallPos] + lis[smallPos+1:]
    return lis

main()