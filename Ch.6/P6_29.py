# Levi VonBank

def main():
    
    # Initializes empty lists to fill with user input
    a = createList('a')
    b = createList('b')
    
    # Prints a new list with the first & second list merged
    print(merge(a, b))

## Creates a loop that appends items to a given list
# @parm takes a number (used for "printing" the list set)
# @return sends back created list
#
def createList(name):
    
    # Initializes an empty list for user input
    lis = []
    
    # loop that reads input and appends it to a list
    print('Enter input for list %s, "Enter" to quit:' % name)
    userInput = input("")
    while userInput != "":
        lis.append(userInput)
        userInput = input("")
    
    return lis

## Merges two lists, alternating elements
# @parm a takes on the first list
# @parm b takes on the second list
# @return sends a merged lists with alternating elements form each list
#
def merge(a, b):
    
    newList = []
    lenA = len(a)
    lenB = len(b)
    
    for i in range(max(lenA, lenB)):
        if i <= lenA-1:
            newList.append(a[i])
        if i <= lenB-1:
            newList.append(b[i])
    
    return newList

main()