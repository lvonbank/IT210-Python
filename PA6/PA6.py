# Levi VonBank

class DooDad:
    _lastNumber = 1000
    _colors = ["red", "green", "blue"]
    
    # Constructs a DooDad
    def __init__(self, color, weight, value):
        self._name = "DooDad"
        
        # Determines the serial number
        DooDad._lastNumber += 1
        self._serialNumber = DooDad._lastNumber
        
        # Verifies & sets color
        color = str(color).lower().strip()
        if color not in DooDad._colors:
            raise RuntimeError('Only "red", "green", "blue" are possible')
        self._color = color
        
        # Verifies & sets value and weight
        try:
            self._weight = float(weight)
            self._value = float(value)
        except ValueError:
            raise TypeError("Weight and/or Value is invalid")
    
    # Returns the serial number
    def getSN(self):
        return self._serialNumber
    
    # Returns the color
    def getColor(self):
        return self._color
    
    # Returns the weight
    def getWeight(self):
        return self._weight
    
    # Returns the value
    def getValue(self):
        return self._value
    
    ## Helper method for choosing color
    # If the colors are the same, that color is used,
    # otherwise the color that is different is used.
    def _getColor(self, rhsDooDad):
        if self._color == rhsDooDad._color:
            color = self._color
        else:
            colors = list(DooDad._colors)
            if self._color in colors:
                colors.remove(self._color)
            if rhsDooDad._color in colors:
                colors.remove(rhsDooDad._color)
            color = colors[0]
        return color
    
    ## + operator
    # If the two serial numbers differ by one, the two
    # values are multiply to get the new value, otherwise
    # they are add. The new DooDad has the color of the left	
    # Doodad and the maximum of the two weights.
    def __add__(self, rhsDooDad):
        if self._serialNumber - rhsDooDad._serialNumber in [1,-1]:
            value = self._value * rhsDooDad._value
        else:
            value = self._value + rhsDooDad._value
        color = self._color
        weight = max(self._weight, rhsDooDad._weight)
        return DooDad(color, weight, value)
    
    ## - operator
    # The new DooDad use the color of the left Doodad,the
    # weight of the right DooDad and the minimum of the two values.
    def __sub__(self, rhsDooDad):
        color = self._color
        weight = rhsDooDad._weight
        value = min(self._value, rhsDooDad._value)
        return DooDad(color, weight, value)
    
    ## * operator
    # The maximum of the two weights, the average of
    # the two values and the color selected by _getColor()
    def __mul__(self, rhsDooDad):
        weight = max(self._weight, rhsDooDad._weight)
        value = (self._value + rhsDooDad._value)/2
        color = self._getColor(rhsDooDad)
        return DooDad(color, weight, value)
    
    ## / operator
    # The same as * except uses the minimum of the two weights.
    def __truediv__(self, rhsDooDad):
        weight = min(self._weight, rhsDooDad._weight)
        value = (self._value + rhsDooDad._value)/2
        color = self._getColor(rhsDooDad)
        return DooDad(color, weight, value)
    
    ## % operator
    # Create a new DooDad whose color is “red”, with a
    # weight that is the sum of both weights and whose value
    # is the weight of the right DooDad.
    def __mod__(self, rhsDooDad):
        weight = self._weight + rhsDooDad._weight
        value = rhsDooDad._weight
        return DooDad("red", weight, value)
    
    ## String Representation
    def __repr__(self):
        return str(self._color) + " " + str(self._name) \
        + " weighing " + str(self._weight).rstrip('0').rstrip('.') \
        + " grams. Value = " + str(self._value).rstrip('0').rstrip('.') \
        + " points. S/N=" + str(self._serialNumber)
        

class DooDadX(DooDad):
    # Constructs a DooDadX
    def __init__(self, color, weight, value):
        super().__init__(color, weight, value)
        self._name = "DooDadX"
        self._serialNumber *= -1
    
    ## %
    # (when the left operand is a DooDadX) it will produce 
    # a green DooDadX whose weight is the maximum of the 
    # two weights. Value is computed the same as for the 
    # % operator in the DooDad class
    def __mod__(self, rhsDooDad):
        weight = max(self._weight, rhsDooDad._weight)
        value = rhsDooDad._weight
        return DooDadX("green", weight, value)


if __name__ == "__main__":
    doodads = []  # will hold both DooDad's and DooDadX's
    doodads.append(DooDad("red",5,10))
    doodads.append(DooDad("red",8,9))
    doodads.append(DooDad("blue",20,15))
    doodads.append(DooDad("green",2,5))
    doodads.append(DooDadX("blue",10,12))
    doodads.append(doodads[0] + doodads[1])
    doodads.append(doodads[2] + doodads[0])
    doodads.append(doodads[3] - doodads[1])
    doodads.append(doodads[1] - doodads[3])
    doodads.append(doodads[0] * doodads[1])
    doodads.append(doodads[0] * doodads[2])
    doodads.append(doodads[0] / doodads[3])
    doodads.append(doodads[2] % doodads[4])
    doodads.append(doodads[4] % doodads[2])

    for doodad in doodads:
        print(doodad)