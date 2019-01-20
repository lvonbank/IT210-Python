# Levi VonBank

try:
    # Prompts the user for file name
    filename = input("Please enter the file name: ")
    
    # Opens files.
    babynames = open(filename , "r")
    boynames = open("boynames.txt", "w")
    girlnames = open("girlnames.txt", "w")
    
    try:  
        line = babynames.readline()
        while line != "":
            dataFields = line.split()
            
            # Raises an exception if line is not correct format 
            if len(dataFields) != 5:
                raise Exception("incorrect number of items")
            
            # Extracts needed data from line
            rank = int(dataFields[0])
            boyName = dataFields[1]
            boyPercent = dataFields[2]
            girlName = dataFields[3]
            girlPercent = dataFields[4]
            
            # Writes the desired data to each file (boy or girl)
            boynames.write("%4d %-12s %s \n" %(rank, boyName, boyPercent))
            girlnames.write("%4d %-12s %s \n" %(rank, girlName, girlPercent))
            
            line = babynames.readline()
    
    finally:
        # Close all files on completion
        babynames.close()
        boynames.close()
        girlnames.close()

except IOError:
    print('Error: file not found')

except Exception as error:
    print('Error:', str(error))