# Levi VonBank

try:
    # Prompts the user for file names
    filename1 = input("Enter first file name: ")
    filename2 = input("Enter second file name: ")
    
    # Opens file.
    inputFile1 = open(filename1 , "r")
    inputFile2 = open(filename2 , "r")
    
    try:
        # Counts the occurrences of words in file 1
        wordset1 = set()
        for line in inputFile1:
            line = line.rstrip()
            wordList = line.split()
            for word in wordList:
                word = word.strip('.,?!')
                wordset1.add(word)
        
        # Counts the occurrences of words in file 2
        wordset2 = set()
        for line in inputFile2:
            line = line.rstrip()
            wordList = line.split()
            for word in wordList:
                word = word.strip('.,?!')
                wordset2.add(word)
        
        commonWords = wordset1.intersection(wordset2)
        for word in sorted(commonWords):
            print(word)

    finally:
        # Close file on completion
        inputFile1.close()
        inputFile2.close()

except IOError:
    print('Error: file not found')