# Levi VonBank

from graphics import GraphicsWindow

# Sets a Constant for window size
SIZE = 400
RESET = 0

# Initializes variables for GraphicsWindow
win = GraphicsWindow(SIZE,SIZE)
canvas = win.canvas()

# Initializes variables for Drawing a Checkerboard
boardLen = 8
boxSize = SIZE / boardLen
x = RESET
y = RESET

# Draws a Checkerboard
for i in range(boardLen):
    for j in range(boardLen):
        if i % 2 == j % 2:
            canvas.setColor("Black")
        else:
            canvas.setColor("White")
        canvas.drawRect(x,y,boxSize,boxSize)
        x += boxSize
    x = RESET
    y += boxSize

# Wait for the user to close the window
win.wait()