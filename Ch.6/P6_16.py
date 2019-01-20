# Levi VonBank

# Imports randint
from random import randint

# Creates an empty lists to fill
randomList = []

# Starts a loop to fill randomList with values
for i in range(20):
    number = randint(0,99)
    randomList.append(number)

# Prints the initial list
print(randomList)

# Sorts randomList & prints it
randomList.sort()
print(randomList)