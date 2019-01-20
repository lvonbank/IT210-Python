# Levi VonBank

# Imports randint
from random import randint

# Creates empty lists to fill
randList = []
evenIndex = []
evenElements = []
reverse = []
first_Last = []

# Starts a loop to fill desired lists with values
for i in range(0,10):
    
    # Uses randint to supply randlist with random values
    num = randint(1,10)
    randList.append(num)
    
    # Determines if index is even and add it to evenIndex list
    if i % 2 == 0:
        evenIndex.append(randList[i])
    
    # Determines if element is even and add it to evenElements list
    if randList[i] % 2 == 0:
        evenElements.append(randList[i])

# Reverses randList
reverse = randList[::-1]

# Puts the first & last values of randList in first_Last list
first_Last = [randList[0], randList[-1]]

# Prints randList, evenIndex, evenElements, reverse, first_Last
print("Random list", randList)
print("Even index", evenIndex)
print("Even elements", evenElements)
print("Reversed", reverse)
print("First & Last", first_Last)