# Levi VonBank

def main():
    try:
        # Prompts for the input file name
        filename = input("Enter the name of the file to display: ")
        data = readFile(filename)
        
        # Obtains and assigns services and there totals to variables
        categories = data[0]
        totalSales = data[1]
        
        # Prints the total sum for each services
        print("Totals:")
        for i in range(len(categories)):
            for j in range(1):
                print("%12s: $ %.2f" %(categories[i], totalSales[i]))
            
    except IOError:
        print('Error: file not found')
        
    except ValueError:
        print('Error: invalid dollar amount')
        
    except RuntimeError as error:
        print('Error:', str(error))
        
    except Exception as error:
        print('Error:', str(error))
    
## Opens a file and read data
# @parm filename the name of the file with data
# @return a list containing data in file
#
def readFile(filename):
    inFile = open(filename, "r")
    try:
        return readData(inFile)
    finally:
        inFile.close()

## Reads a data set
# @parm inFile the input file containing the data
# @return data set in list
#
def readData(inFile):
    # Initializes empty lists
    data = []
    categories = []
    sales = []
    totalSales = []
    
    line = inFile.readline()

    # Raises an exception if file is empty
    if line == "":
        raise Exception("empty file")
    
    # Loops for every line until "" is reached
    while line != "":
        
        if ';' in line:
            dataFields = line.split(';')
            
            # Raises an exception if line is not correct format 
            if len(dataFields) != 4:
                raise Exception("incorrect number of items")

            # Reads services and appends them to categories
            variable = dataFields[1]
            if variable not in categories:
                categories.append(variable)
                sales.append([])
            
            # Reads dollar amounts and appends them to sales
            amount = float(dataFields[2])
            for i in range(len(categories)):
                if categories[i] == variable:
                    sales[i].append(amount)
        
        else: raise Exception("format is invalid")
                    
        line = inFile.readline()
    
    # Adds up all values in each category of sales
    total = 0
    for i in range(len(sales)):
        for j in range(len(sales[i])):
            total += sales[i][j]
        totalSales.append(total)
        total = 0
    
    # Appends final results to a list for the return
    data.append(categories)
    data.append(totalSales)
    
    return data

main()