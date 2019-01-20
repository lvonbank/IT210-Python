# Levi VonBank

# Draw a house
#
# import necessary graphics functionality provided by the authors from graphics import GraphicsWindow
from graphics import GraphicsWindow

# Create the graphics window named win
win = GraphicsWindow(400,400)

# Create a canvas we can draw on
canvas = win.canvas()

# Draw the house. Change this if you want to draw a different style house
canvas.setColor("red")
canvas.drawRect(100,150,200,200)
# Add your python code to complete the house drawing here...

# House texture

# Vertical lines
canvas.setColor("Magenta")
canvas.drawLine(100,170,300,170)
canvas.drawLine(100,190,300,190)
canvas.drawLine(100,210,300,210)
canvas.drawLine(100,230,300,230)
canvas.drawLine(100,250,300,250)
canvas.drawLine(100,270,300,270)
canvas.drawLine(100,290,300,290)
canvas.drawLine(100,310,300,310)
canvas.drawLine(100,330,300,330)

# Horizontal lines
canvas.drawLine(120,150,120,350)
canvas.drawLine(140,150,140,350)
canvas.drawLine(160,150,160,350)
canvas.drawLine(180,150,180,350)
canvas.drawLine(200,150,200,350)
canvas.drawLine(220,150,220,350)
canvas.drawLine(240,150,240,350)
canvas.drawLine(260,150,260,350)
canvas.drawLine(280,150,280,350)

# Door
canvas.setColor("brown")
canvas.drawRect(140,250,50,100)

# Door knob
canvas.setColor("yellow")
canvas.drawOval(180,300,5,5)

# House window
canvas.setColor("green")
canvas.drawRect(220,270,50,50)
canvas.setColor("blue")
canvas.drawLine(245,270,245,320)
canvas.drawLine(220,295,270,295)

# Roof boundary lines
canvas.setColor("red")
canvas.drawLine(200,50,100,150)
canvas.drawLine(200,50,300,150)

# Roof fill
canvas.setColor("purple")
canvas.drawPoly(100,150,200,50,300,150)

# Sign saying "Welcome Home"
canvas.setColor("orange")
canvas.drawRect(150,185,101,25)
canvas.setColor("black")
canvas.drawText(155,190,"Welcome Home")

# Creates a stick person
canvas.setColor(255,204,153)
canvas.drawOval(310,250,30,30) # Head
canvas.setColor("black")
canvas.drawLine(325,320,325,280) # Body
canvas.drawLine(325,320,310,350) # Left leg
canvas.drawLine(325,320,340,350) # Right Leg
canvas.drawLine(325,300,310,300) # Left arm
canvas.drawLine(325,300,340,300) # Right arm
canvas.drawOval(317,260,3,3) # Left eye
canvas.drawOval(327,260,3,3) # Right eye
canvas.drawOval(320,270,6,3) # Mouth


# This statement will make the window stay open until its "close" button is clicked
win.wait()