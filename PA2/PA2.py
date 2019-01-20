# Levi VonBank

# Imports the command to exit program
from sys import exit

# Creates constants for ROW & COLUMN
ROW = 4
COLUMN = 4

def main():
    # Creates an empty list
    table = []
    
    # Reads the input values
    for i in range(ROW):
        row = []
        table.append(row)
        for j in range(COLUMN):
            userInput = input("Enter a value for location (%s,%s): " %(i,j))
            
            # Validates entry and/or adds it to the table
            if not (userInput.isdigit()) or len(userInput) > 2:
                exit("Your entry was an unacceptable input.")
            else: row.append(int(userInput))

    # Adds up column total
    columnTotal = []
    ctotal = 0
    for j in range(COLUMN):
        ctotal = 0
        for i in range(ROW):
            ctotal += int(table[i][j])
        columnTotal.append(ctotal)

    # Adds up row total
    rowTotal = []
    rtotal = 0
    for i in range(ROW):
        rtotal = 0
        for j in range(COLUMN):
            rtotal += int(table[i][j])
        rowTotal.append(rtotal)

    # Adds up right diagnal
    rightTotal = 0
    j = COLUMN - 1
    for i in range(ROW):
        rightTotal += table[i][j]
        j = j - 1
    rightDiag = [rightTotal]

    # Adds up left diagnal
    leftTotal = 0
    i = 0
    for j in range(COLUMN):
        leftTotal += table[i][j]
        i = i + 1
    leftDiag = [leftTotal]

    # Prints matrix
    for i in range(ROW):
        for j in range(COLUMN):
            print("%3d" % table[i][j], end="")
        print()
    
    # Crosschecks userInput for 1, 2, ..., 16
    contentVal = validNumbers(table)

    # Validates that all rows, columns, and diagonals equal the same
    finalListTotal = columnTotal + rowTotal + rightDiag + leftDiag
    totalVal = equalityCheck(finalListTotal)

    # Determines if it is a magic square or not
    if contentVal and totalVal:
        valid = ""
    else: 
        valid = " not"

    # Prints result
    print("It is%s a magic square." % valid)

## Creates a list of 1, 2, ..., 16 & crosschecks it with userInput
# @parm table obtains users table for crosschecking
# @return send back boolean based on results
def validNumbers(table):
    # Creates a version of the usersInput without sub lists
    testList = []
    for i in range(ROW):
        for j in range(COLUMN):
            testList.append(table[i][j])
    testList.sort()  # Sorts it new list for crosschecking
    
    # Produces a list of 1, 2, ..., 16 to cross-reference with
    validTable = []
    numbers = 0
    for i in range(ROW):
        for j in range(COLUMN):
            numbers += 1
            validTable.append(int(numbers))
    
    # Checks users list to validate content (the use of 1, 2, ..., 16)
    # Sent back True only if it matches requirements
    if testList == validTable:
        return True
    else: return False

## Determines if all the values in a list are the same
# @parm checklist obtains a list for crosschecking
# @return send back boolean based on results
def equalityCheck(checklist):
    count = 0
    length = len(checklist)-1
    for i in range(length):
        if checklist[i] == checklist[i+1]:
            count += 1
    if count == (length):
        return True
    else: return False

main()