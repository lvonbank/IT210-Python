# Levi VonBank

def main():
    try:
        elevMatrix = readTerrain()
        printTerrain(elevMatrix)
        
        count = 1
        with open("flood.txt", "r") as inFile:
            for line in inFile:
                line = line.strip()
                if line != "":
                    try:
                        h2oElevation = int(line)
                        print("\nFlooding at elevation =", h2oElevation)
                        floodMatrix = calcFlood(elevMatrix, h2oElevation)
                        printFlood(floodMatrix)
                    except ValueError:
                        print('\nError: invalid integer "%s" on line %d' %(line,count))
                count += 1
            
    except IOError as error:
        print('\nError: missing file(s)')
        
    except RuntimeError as error:
        print('\nError:', str(error))
        
    except Exception as error:
        print('\nError:', str(error))

## Open/Closes & reads terrain.txt
# @return matrix (a list of lists)
def readTerrain():
    elevMatrix = []
    with open("terrain.txt", "r") as inFile:
        for line in inFile:
            line = line.strip()
            dataFields = line.split(' ')
            
            # Removes empty strings if present
            i = 0
            while i < len(dataFields):
                if dataFields[i] == '':
                    dataFields.pop(i)
                else: i += 1
                    
            elevMatrix.append(dataFields)
        
    return elevMatrix

## Prints a map of terrain elevations
# @elevMatrix is a matrix of elevations from terrain.txt
def printTerrain(elevMatrix):
    for row in range(len(elevMatrix)):
        for column in range(len(elevMatrix[row])):
            print("%4s" %(elevMatrix[row][column]), end="")
        print()

## Constructs a table of flooded elevations from in correlation to terrain
# @elevMatrix is a matrix of elevations from terrain.txt
# @h2oElevation level of flooding from flood.txt
def calcFlood(elevMatrix, h2oElevation):
    floodMatrix = []
    
    # Constructs flood matrix
    for row in range(len(elevMatrix)):
        floodMatrix.append([])
        for column in range(len(elevMatrix[row])):
            try:
                if int(elevMatrix[row][column]) <= h2oElevation:
                    floodMatrix[row].append("*")
                else:
                    floodMatrix[row].append(" ")
            except ValueError:
                floodMatrix[row].append("-")
                
    return floodMatrix

## Prints the matrix returned by calcFlood
# @floodMatrix is a matrix of flooded elevations in comparison to terrain
def printFlood(floodMatrix):
    for row in range(len(floodMatrix)):
        for column in range(len(floodMatrix[row])):
            print("%4s" %(floodMatrix[row][column]), end="")
        print()
    
main()