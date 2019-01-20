# Levi VonBank

# Imports randint to imitate actual tolerance of a resister
from random import randint

## Provides a description of a 4 band resister give its colors
class Resistor:

    ## Constructs detailed info on the resister based on its colors
    # @color1 obtains the first color of the resister
    # @color2 obtains the second color of the resister
    # @color3 obtains the third color of the resister
    # @color4 obtains the fourth color of the resister
    def __init__(self, color1, color2, color3, color4=""):
        colorCode = {'Black':['0',0,'-'], 'Brown':['1',1,0.01],
                     'Red':['2',2,0.02], 'Orange':['3',3,'-'],
                     'Yellow':['4',4,'-'], 'Green':['5',5,0.005],
                     'Blue':['6',6,0.0025], 'Violet':['7',7,0.001],
                     'Gray':['8',8,0.0005], 'White':['9',9,'-'],
                     'Gold':['-',-1,0.05], 'Silver':['-',-2,0.1]}

        # Gives a description on errors
        error1 = "has no significant digit"
        error2 = "has no attribute for tolerance"
        error3 = "Unsupported Input Given"
        
        # Determines what the first three bands mean
        if color1 and color2 and color3 in colorCode:
            key = colorCode[color1]      # First band
            if key[0] == '-':
                raise RuntimeError("%s %s" %(color1, error1))
            self._digit1 = key[0]
            key = colorCode[color2]      # Second band
            if key[0] == '-':
                raise RuntimeError("%s %s" %(color2, error1))
            self._digit2 = key[0]
            key = colorCode[color3]      # Third band
            self._multiplier = key[1]
        else: raise RuntimeError(error3)
        
        if color4 in colorCode:
            key = colorCode[color4]      # Fourth band
            if key[2] == '-':
                raise RuntimeError("%s %s" %(color4, error2))
            self._tolerance = key[2]
        elif color4 == "":
            self._tolerance = 0.2
        else: raise RuntimeError(error3)

    ## Produces a string with pertinent information on the band
    # @return a string of information about the bands
    def getDescription(self):
        nominal = str(self.getNominal())
        tolerance = str(self._tolerance * 100)
        return ("|%s ohms|+-%s%%|" % (nominal, tolerance))

    ## Calculates the nominal number of the bands
    # @return nominal value
    def getNominal(self):
        return int(self._digit1 + self._digit2)*10**(self._multiplier)
    
    ## A randomized range of an actual resistance
    # @return actual value
    def getActual(self):
        nominal = self.getNominal()
        offset = nominal * self._tolerance
        randnum = randint(-offset, offset)
        return nominal + randnum


if __name__ == "__main__":
    
    def main():
        print("Bands: Red, Violet, Green, Gold")
        testRun(Resistor('Red','Violet','Green','Gold'))
    
        print() # Breaks up information
        
        print("Bands: Black, Orange, Green")
        testRun(Resistor('Black','Orange','Green'))
        
        print() # Breaks up information
    
        try:
            Resistor('Silver','Blue','Yellow', 'Gold')
        except RuntimeError as error:
            print('Error:', str(error))
    
        try:
            Resistor('White','Brown','Yellow', 'Orange')
        except RuntimeError as error:
            print('Error:', str(error))
    
        try:
            Resistor('Violet','Green','Hi', 'Orange')
        except RuntimeError as error:
            print('Error:', str(error))
        
    def testRun(resistor):
        print("Description:", resistor.getDescription())
        print("Nominal: %d ohms" %resistor.getNominal())
        print("Actual: %d ohms" %resistor.getActual())
    
    main()