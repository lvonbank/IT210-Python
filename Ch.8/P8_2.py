# Levi VonBank

try:
    # Prompts the user for file names
    filename = input("Please enter the file name: ")
    
    # Opens file.
    inputFile = open(filename , "r")
    
    try:
        # Counts the occurrences of words
        words = {}
        line = inputFile.readline()
        while line != "" :
            line = line.rstrip()
            wordList = line.split()
            for word in wordList:
                word = word.strip('.,?!')
                if word not in words:
                    words[word] = 1
                else: words[word] += 1
            line = inputFile.readline()
        
        for (key, value) in sorted(words.items()):
            print(key, value)

    finally:
        # Close file on completion
        inputFile.close()

except IOError:
    print('Error: file not found')