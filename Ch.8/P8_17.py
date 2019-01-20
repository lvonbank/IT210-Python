# Levi VonBank

try:
    # Prompts the user for file names
    filename = input("Enter a file name: ")
    
    # Opens file.
    inputFile = open(filename , "r")
    
    try:
        countryPCI = {}
        
        # Extracts data from file
        for line in inputFile:
            dataFields = line.split('\t')
            
            # Raises an exception if line is not correct format 
            if len(dataFields) != 3:
                raise Exception("incorrect number of items")
                
            country = dataFields[1].lower()
            perCapIncome = dataFields[2].replace(' ','')
            
            # Applies data to dictionary
            countryPCI[country] = perCapIncome
            
        print("Enter country name or quit:")
        name = input("").lower()
        while name.lower() != 'quit':
            if name in countryPCI:
                print(countryPCI[name])
            else:
                print("Unrecognized Country Name")
            name = input("").lower()
    
    finally:
        # Close file on completion
        inputFile.close()

except IOError:
    print('Error: file not found')

except Exception as error:
    print('Error:', str(error))