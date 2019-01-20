# Levi VonBank

try:
    # Prompts the user for file names
    filename = input("Please enter the file name: ") 
    
    # Open the file.
    inFile = open(filename, "r")
    
    try:
        # Initializes counters
        charcount = 0
        wordcount = 0
        linecount = 0
        
        # Loops over each line
        for line in inFile:
            line = line.rstrip()
            wordList = line.split()
            linecount += 1 
            wordcount += len(wordList)
            charcount += len(line)
        
        print("There is %s characters" % charcount)
        print("There is %s words" % wordcount)
        print("There is %s lines" % linecount)
    
    finally:
        # close file on completion
        inFile.close()

except IOError:
    print('Error: file not found')