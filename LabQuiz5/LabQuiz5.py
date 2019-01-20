# Levi VonBank

# Your code goes here
class Apartment:
    def __init__(self, aptNumber, address, bedrooms, baths):
        self._aptNumber = str(aptNumber)
        self._address = str(address)
        try:
            self._bedrooms = int(bedrooms)
            self._baths = float(baths)
        except ValueError:
            raise ValueError("Bedrooms/Baths is not valid")
        self._securityDep = (330.0 * self._bedrooms)
        self._rent = (250.0 * self._bedrooms) + (150.0 * self._baths) + 200.0
        self._renter = "vacant"
    
    def setSecDep(self, securityDep):
        try:
            self._securityDep = float(securityDep)
        except ValueError:
            raise ValueError("Security deposit is not valid")
    
    def setRent(self, rent):
        try:
            self._rent = float(rent)
        except ValueError:
            raise ValueError("Rent is not valid")
    
    def setRenter(self, renter):
        if renter in [" ", ""]:
            self._renter = "vacant"
        else:
            self._renter = renter
    
    def getData(self):
        return "Apt " + self._aptNumber + " located at " + self._address + "\n" \
        + str(self._bedrooms) + " bedrooms and " + str(self._baths) + " baths" + "\n" \
        + "$" + str(self._securityDep) + " security deposit and $" + str(self._rent) + "\n" \
        + "Rented to: " + str(self._renter)
    
    def isVacant(self):
        if self._renter == "vacant":
            return True
        return False
    
    def __repr__(self):
        if self.isVacant():
            rented = "vacant"
        else: 
            rented = "rented"
        return "Apt " + self._aptNumber + " @ " + self._address + " " + str(self._bedrooms) \
        + " BR " + str(self._baths) + " Baths  Dep=$" + str(self._securityDep) + "  Rent=$" \
        + str(self._rent) + "  " + rented

# Test code for the Apartment Class
if __name__ == "__main__":
    apts = []
    apts.append(Apartment("10C", "107 E. Main", 3, 1.5))
    apts.append(Apartment("14B", "109 E. Main", 4, 2))
    apts.append(Apartment("13", "2207 W. Broadway", "5", "2.5"))
    
    for apt in apts:
        print(apt)
    print()
    
    apts[0].setRent("1245")
    apts[0].setRenter("Rocky Quartzite")
    apts[1].setSecDep("1000")
    apts[1].setRenter("Millie Milton")
    
    print(apts[0].getData())
    print()
    
    for apt in apts:
        if not apt.isVacant():
            print(apt)
    print()
    
    apts[0].setRenter("")
    print(apts[0])
