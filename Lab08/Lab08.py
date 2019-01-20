# Levi VonBank
# Group Members: Scott Fleming

## Logs information on give toys
class Toy():
    _catalog = []
    _barCode = 1000
    _byBarCode = {}
    _byName = {}
    
    ## Constructs default attributes
    # @parm toyName gives  the toy a name
    def __init__(self, toyName):
        Toy._barCode += 1
        Toy._catalog.append(toyName)
        Toy._byBarCode[Toy._barCode] = toyName
        Toy._byName[toyName] = Toy._barCode
        self._toyName = toyName
        self._price = 0.0
        self._gender = "Either"
        self._MinAge = "Rated-E (for everyone)"
    
    ## Sets a price
    # @parm price is the cost
    def setPrice(self, price):
        try:
            newPrice = float(price)
            self._price = round(newPrice,2)
        except ValueError:
            raise ValueError("Price isn't a valid number")
    
    ## Retuns a price
    def getPrice(self):
        return self._price
    
    ## Sets a gender
    # @parm gender is gender interest
    def setGender(self, gender):
        self._gender = gender
        
    ## Retuns a gender
    def getGender(self):
        return self._gender
    
    ## Sets minimum for recommended age
    # @parm minAge a give age
    def setMinAge(self, minAge):
        self._MinAge = minAge
    
    ## Retuns a minimum age
    def getMinAge(self):
        return self._MinAge
    
    ## String/Print representation
    def __repr__(self):
        return str(self._toyName) + " is " + "$" + str(self._price) \
               + " designed for " + str(self._gender) \
               + " recommended for age(s) " + str(self._MinAge)
    
    ## Determines if gift wrapping is available
    def giftWrap(self):
        if self._price > 50:
            return True
        else: return False
    
    ## Returns a list of all items of toys
    def getCatalog():
        return Toy._catalog
    
    ## Search for barcode by name
    # @parm name searching barcode
    def searchByName(name):
        if name in Toy._byName:
            return Toy._byName[name]
        else: return "NA"
    
    ## Search for name by barcode
    # @parm barcode searching name
    def searchByBarcode(barcode):
        if barcode in Toy._byBarCode:
            return Toy._byBarCode[barcode]
        else: return "NA"

if __name__ == "__main__":
    toy1 = Toy("Robot")
    toy1.setPrice(70)
    toy1.setGender("Males")
    print('Gender:',toy1.getGender())
    toy1.setMinAge(5)
    print(toy1)

    print()
    
    toy2 = Toy("Barbie")
    print('Price:',toy2.getPrice())
    toy2.setPrice(0.01)
    print('Gender:',toy2.getGender())
    toy2.setGender("Females")
    print(toy2)
    
    print()
    
    toy3 = Toy("Stuffed Animal")
    toy3.setMinAge(1)
    print('MinAge:',toy3.getMinAge())
    print(toy3)
    
    print()
    
    print("GiftWrap:",toy1.giftWrap())
    print("Barbie =",Toy.searchByName("Barbie"))
    print("1001 =",Toy.searchByBarcode(1001))
    print("Toy Catalog:",Toy.getCatalog())