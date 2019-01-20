# Levi VonBank

try:
    # Prompts the user for file name
    filename = input("Please enter the file name: ")
    
    # Opens files.
    babynames = open(filename , "r")
    
    try:
        boyNames = []
        girlNames = []
        
        line = babynames.readline()
        while line != "":
            dataFields = line.split()
            
            # Raises an exception if line is not correct format 
            if len(dataFields) != 5:
                raise Exception("incorrect number of items")
            
            # Extracts needed data from line
            boyNames.append(dataFields[1])
            girlNames.append(dataFields[3])
            
            line = babynames.readline()
        
        # Prints names that are both boy and girl
        for i in range(len(boyNames)):
            for j in range(len(girlNames)):
                if boyNames[i] == girlNames[j]:
                    print(boyNames[i])
    
    finally:
        # Close all files on completion
        babynames.close()

except IOError:
    print('Error: file not found')

except Exception as error:
    print('Error:', str(error))