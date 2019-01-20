# Levi VonBank

## Simulates a bugs movement in relation to its coordinates and direction
class Bug():
    ## Constructs initial coordinates and direction
    # @parm initPos given position
    # @parm initDir given direction
    def __init__(self, initPos = (0, 0), initDir = 'N'):
        defultDir = 'N'
        if initDir != '' and type(initDir) == str:
            if initDir[0].upper() in "NEWS":
                self._dir = initDir[0].upper()
            else: self._dir = defultDir
        else: self._dir = defultDir
        
        # Test if initPos is a valid tuple
        if type(initPos)!= tuple:
            raise TypeError("coordinate(s) aren’t a tuple")
        try:
            self._posX = int(initPos[0])
            self._posY = int(initPos[1])
        except ValueError:
            raise ValueError("coordinate(s) aren’t integers")
    
    ## Justifies new direction when turning right
    def turnRight(self):
        if self._dir == 'N':
            self._dir = 'E'
        elif self._dir == 'E':
            self._dir = 'S'
        elif self._dir == 'S':
            self._dir = 'W'
        elif self._dir == 'W':
            self._dir = 'N'
    
    ## Justifies new direction when turning left
    def turnLeft(self):
        if self._dir == 'N':
            self._dir = 'W'
        elif self._dir == 'E':
            self._dir = 'N'
        elif self._dir == 'S':
            self._dir = 'E'
        elif self._dir == 'W':
            self._dir = 'S'
    
    ## Justifies new direction when turning around
    def uTurn(self):
        if self._dir == 'N':
            self._dir = 'S'
        elif self._dir == 'E':
            self._dir = 'W'
        elif self._dir == 'S':
            self._dir = 'N'
        elif self._dir == 'W':
            self._dir = 'E'
    
    ## Moves bug forward by 1
    def move(self):
        if self._dir == 'N':
            self._posY += 1
        elif self._dir == 'E':
            self._posX += 1
        elif self._dir == 'S':
            self._posY -= 1
        elif self._dir == 'W':
            self._posX -= 1
    
    ## Moves bug forward by given amount
    # @parm count desired amount to move
    def moveMulti(self, count):
        try:
            moveX = int(count)
        except ValueError:
            raise ValueError("moveMulti takes only integers")
        
        if self._dir == 'N':
            self._posY += moveX
        elif self._dir == 'E':
            self._posX += moveX
        elif self._dir == 'S':
            self._posY -= moveX
        elif self._dir == 'W':
            self._posX -= moveX
    
    ## Set a new position
    # @parm posTuple new position
    def setPos(self, posTuple):
        # Test if posTuple is a valid tuple
        if type(posTuple)!= tuple:
            raise TypeError("coordinate(s) aren’t a tuple")
        try:
            self._posX = int(posTuple[0])
            self._posY = int(posTuple[1])
        except ValueError:
            raise ValueError("coordinate(s) aren’t integers")
    
    ## Returns position
    def getPos(self):
        return (self._posX, self._posY)
    
    ## Sets a direction
    def setDir(self, dirStr):
        if dirStr != '' and type(dirStr) == str:
            if dirStr[0].upper() in "NEWS":
                self._dir = dirStr[0].upper()
    
    ## Returns direction
    def getDir(self): # returns a direction string
        if self._dir == 'N':
            direction = 'north'
        elif self._dir == 'E':
            direction = 'east'
        elif self._dir == 'S':
            direction = 'south'
        elif self._dir == 'W':
            direction = 'west'
        return direction
    
    def __repr__(self):
        return "Bug at " + str(self.getPos()) + " facing " + str(self.getDir())

if __name__ == "__main__":
    bugsy = Bug((0,1),'west')
    bugsy.move() # (-1,1), 'W'
    bugsy.uTurn() # 'E'
    bugsy.turnLeft() # 'N'
    bugsy.move() # (-1,2), 'N'
    print('Excepted: (-1, 2) |',bugsy.getPos()) # (-1,2)
    bugsy.setPos((0,5)) # (0,5), 'N'
    bugsy.turnRight() # 'E'
    print('Excepted: east |',bugsy.getDir()) # 'east'
    bugsy.move() # (1,5), 'E'
    bugsy.setDir('North!!') # 'N'
    bugsy.moveMulti(5) # (1,10), 'N'
    print(bugsy)
    
    print()
    
    bugse = Bug()
    print(bugse)
    print('Excepted: (0, 0) |',bugse.getPos())
    print('Excepted: north |',bugse.getDir())
    
    