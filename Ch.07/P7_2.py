# Levi VonBank

try:
    # Prompts the user for file names
    inFilename = input("Please enter the input file name: ")
    outFilename = input("Please enter the output file name: ")
    
    # Open the files.
    inFile = open(inFilename, "r")
    outFile = open(outFilename, "w")
    
    try:
        # Reads each line
        count = 1    
        line = inFile.readline()
        while line != "":
            # Writes each line with a line number to the out file
            outFile.write("/* %d */ %s" % (count, line))
            count += 1
            line = inFile.readline()
    
    finally:
        # Close each file on completion
        inFile.close()
        outFile.close()

except IOError:
    print('Error: file not found')