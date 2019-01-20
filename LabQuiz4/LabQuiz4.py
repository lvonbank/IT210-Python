# Levi VonBank

class Pencil :
    # All strings except stockNum & hardness stored lowercase
    # initial values: color and profile are empty strings
    # initial values: cost: $0.00, eraser: "regular"
    # stockNum and hardness are strings
    def __init__(self, stockNum, hardness):
        self._stockNum = stockNum
        self._hardness = hardness
        self._color = ''
        self._profile = ''
        self._eraser = 'regular'
        self._cost = '0.00'

    def setColor(self, color): # color is a string.
        self._color = str(color).lower()

    # profile is a string (typically "round" or "hex")
    def setProfile(self, profile):
        self._profile = str(profile).lower()

    def setCost(self, cost): # A float
        try:
            newCost = float(cost)
            self._cost = round(newCost, 2)
        except ValueError:
            raise ValueError("Cost isn't a valid number")

    # eraser is a string (typ. "no" or "regular" or "jumbo")
    def setEraser(self, eraser):
        self._eraser = str(eraser).lower()

    def getColor(self):
        return self._color

    def getProfile(self):
        return self._profile

    def getCost(self):
        return float(self._cost)

    def getEraser(self):
        return self._eraser

    # Include color, profile, stockNum, hardness and cost
    def __repr__(self): # Include color, profile, stockNum, hardness and cost
        return str(self._color) + " " + str(self._profile) \
               + " Pencil, stock#: " + str(self._stockNum) + ", hardness: " \
               + str(self._hardness) + ", cost: $" + str(self._cost)

# Make NO CHANGES to the following test code!!
if __name__ == "__main__":
    pencils = []
    pencils.append(Pencil("X23B", "2H"))
    pencils.append(Pencil("ZZ7", "3"))
    pencils.append(Pencil("ABC", "2"))
    pencils.append(Pencil("4-H", "4"))

    for pencil in pencils:
        print(pencil)
    print()

    colors = ["Red", "WHITE", "blue"]
    profiles = ['hex', 'HEX', "Round"]
    costs = [0.06,.25,.49]
    erasers = ['none','JUMBO',"Regular"]
    for i in range(3):
        pencils[i].setColor(colors[i])
        pencils[i].setProfile(profiles[i])
        pencils[i].setCost(costs[i])
        pencils[i].setEraser(erasers[i])

    for pencil in pencils:
        print(pencil)
        print("Color: %s   Cost: $%0.2f" % \
             (pencil.getColor(),pencil.getCost()))
        print("Profile: %s   Eraser: %s" % \
             (pencil.getProfile(),pencil.getEraser()))
        print()

