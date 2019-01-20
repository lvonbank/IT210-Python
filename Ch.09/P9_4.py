# Levi VonBank

## Constructs an address
class Address:
    
    ## Builds address
    # @parm houseNumber obtains the number of the house
    # @parm street obtains the street
    # @parm city obtains the city
    # @parm state obtains the state
    # @parm zipCode obtains the zip
    # @parm apartment obtains a suit (optional)
    def __init__(self, houseNumber, street, city, state, zipCode, apartment=''):
        self._houseNumber = str(houseNumber)
        self._street = str(street)
        self._city = str(city)
        self._state = str(state)
        self._zipCode = str(zipCode)
        self._apartment = str(apartment)

    # Returns a boolean for testing the smallest zipcode
    def comesBefore(self, other):
        return self._zipCode < other._zipCode
    
    # Prints directly to the terminal
    def prints(self):
        print(self)

    # The representation of the address as a string
    def __repr__(self):
        return self._houseNumber +' '+ self._street +' '+ self._apartment \
               + "\n" + self._city +' '+ self._state +' '+ self._zipCode


if __name__ == "__main__":
    
    addr1 = Address(123, 'Fake Street', 'Mankato', 'MN', 56001, 'Apt. 11')
    addr1.prints()
    
    print() # Breaks up information
    
    addr2 = Address(23455, 'Wrong way Blvd.', 'Belle Plaine', 'MN', 56011)
    addr2.prints()
    
    print() # Breaks up information
    
    print(addr1.comesBefore(addr2))
    print(addr2.comesBefore(addr1))