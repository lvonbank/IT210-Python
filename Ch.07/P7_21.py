# Levi VonBank

from string import ascii_uppercase

# Creates constance for table
ROW = 4
COLUMN = 7

try:
    # Prompts the user for file name
    filename = input("Please enter the file name: ")
    
    # Opens files.
    inputFile = open(filename, "r")
    
    try:
        # Reads every character in the file
        total = 0
        letterCounts = [0] * 26
        char = inputFile.read(1)
        while char != "" :
            char = char.upper()   # Convert the character to uppercase.
            if char >= "A" and char <= "Z" :   # Make sure the character is a letter.
                total += 1
                code = ord(char) - ord("A")
                letterCounts[code] = letterCounts[code] + 1
            char = inputFile.read(1)
        
        # Calculates the frequencies
        frequencies = [0] * 26
        frequencies.extend(" " * 2)
        for i in range(len(letterCounts)):
                percentage = round((letterCounts[i] / total) * 100, 1)
                frequencies[i] = str(percentage) + "%"
        
        # Creates a list of the alphabet 
        letters = []
        letters.extend(ascii_uppercase + " " * 2)
        
        # Constructs the table
        c = 0
        frequenciesList = [[],[],[],[]]
        lettersList = [[],[],[],[]]
        for i in range(ROW):
            for j in range(COLUMN):
                lettersList[i].append(letters[c])
                frequenciesList[i].append(frequencies[c])
                c += 1

        # Prints the table
        for i in range(COLUMN):
            for j in range(ROW):
                print("%4s" %(lettersList[j][i]), end="")
                print("%7s" %(frequenciesList[j][i]), end="")
            print()
    
    finally:
        # Close all files on completion
        inputFile.close()

except IOError:
    print('Error: file not found')

