# Levi VonBank

# Prompts the user for file names
inFilename = input("Enter a file name: ")
    
# Open the files.
inFile = open(inFilename, "r")

# Initializes empty lists with equivalent counters
list1 = []
list2 = []
count1 = 0
count2 = 0

# Reads the file containing integers
line = inFile.readline()
while line != "":
    list1.append(int(line))
    count1 += 1
    if int(line) >= 0:
        list2.append(int(line))
        count2 += 1
    line = inFile.readline()

# Closes file upon reading completion
inFile.close()

# Calculates the sum, min, max, & average of list1
list1sum = sum(list1)
list1min = min(list1)
list1max = max(list1)
list1ave = 0
if count1 > 0:
    list1ave = list1sum / count1

# Calculates the sum, min, max, & average of list2
list2sum = sum(list2)
list2min = min(list2)
list2max = max(list2)
list2ave = 0
if count2 > 0:
    list2ave = list2sum / count2

# Prints final results in a table format
print("           list1   list2")
print("sum:     %7d %7d" %(list1sum, list2sum))
print("minimum: %7d %7d" %(list1min, list2min))
print("maximum: %7d %7d" %(list1max, list2max))
print("average: %7.3f %7.3f" %(list1ave, list2ave))

# Creates a sorted list3 with nonmatching numbers form list1
list3 = list(set(list1))
list3.sort()
list3len = len(list3)

# Prints list3 and its length
print()
print("length of list3:", list3len)
print(list3)