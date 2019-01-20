# Levi VonBank

from sys import argv 

try:
    inFile = ""
    outFile = ""
    
    # Obtains command line arguments
    files = 0
    for i in range(1, len(argv)) :
        arg = argv[i] 
        
        files = files + 1
        if files == 1 :
            inFile = arg
        if files == 2 :
            outFile = arg
        
    # There must be two files.
    if files != 2 :
        raise Exception("incorrect number of arguments")
            
    # Opens each file.
    inputFile = open(inFile, "r")
    outputFile = open(outFile, "w")
    
    try:
        # Puts lines in reverse order
        lineList = inputFile.readlines()
        revList = lineList[::-1]
        for elements in revList:
            outputFile.write(elements)
        
    finally:
        # close files on completion
        inputFile.close()
        outputFile.close()

except IOError:
    print('Error: file not found')

except Exception as error:
    print('Error:', str(error)) 