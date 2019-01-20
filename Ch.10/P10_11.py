# Levi VonBank

##
#  This modules defines a class hierarchy for geometric shapes.
#

import graphics

## A basic geometric shape.
#
class GeometricShape :
   ## Construct a basic geometric shape.
   #  @param x the x-coordinate of the shape
   #  @param y the y-coordinate of the shape
   #
   def __init__(self, x, y) :
      self._x = x
      self._y = y
      self._fill = None
      self._outline = "black"

   ## Gets the leftmost x-position of the shape.
   #  @return the x-coordinate
   #
   def getX(self) :
      return self._x

   ## Gets the topmost y-position of the shape.
   #  @return the y-coordinate
   #
   def getY(self) :
      return self._y

   ## Gets the width of the shape.
   #  @return the width
   #
   def getWidth(self) :
      return 0

   ## Gets the height of the shape.
   #  @return the height
   #
   def getHeight(self) :
      return 0

   ## Sets the fill color.
   #  @param color the fill color
   #
   def setFill(self, color = None) :
      self._fill = color

   ## Sets the outline color.
   #  @param color the outline color
   #
   def setOutline(self, color = None) :
      self._outline = color

   ## Sets both the fill and outline colors to the same color.
   #  @param color the new color
   #
   def setColor(self, color) :
      self._fill = color
      self._outline = color

   ## Moves the shape to a new position by adjusting its (x, y) coordinates.
   #  @param dx the amount to move in x-direction
   #  @param dy the amount to move in y-direction
   #
   def moveBy(self, dx, dy) :
      self._x = self._x + dx
      self._y = self._y + dy

   ## Draws the shape on a canvas.
   #  @param canvas the graphical canvas on which to draw the shape
   #
   def draw(self, canvas) :
      canvas.setFill(self._fill)
      canvas.setOutline(self._outline)

## An arbitrary polygon shape.
#
class Polygon(GeometricShape) :
   ## Construct a new polygon from a list of points.
   #  @param vertexList the list of vertices that make up the shape
   #
   def __init__(self, vertexList) :
      # Find the minimum x and y values in the polygon.
      mx = vertexList[0][0]
      my = vertexList[0][1]
      for i in range(len(vertexList)) :
          if vertexList[i][0] < mx :
              mx = vertexList[i][0]
          if vertexList[i][1] < my :
              my = vertexList[i][1]

      # Use the super class constructor to build a new shape at the (mx, my).
      super().__init__(mx, my)

      # Adjust all of the points in the polygon by (mx, my) so that it draws
      # at the correct location.
      self._points = list(vertexList)
      for i in range(len(vertexList)) :
          self._points[i][0] -= mx
          self._points[i][1] -= mx

   ## Overrides the superclass method.
   def getWidth(self) :
      # Find the maximum x value in the polygon -- that's the width.
      mx = self._points[0][0]
      for i in range(len(self._points)) :
          if self._points[i][0] > mx :
              mx = self._points[i][0]
      return mx

   ## Overrides the superclass method.
   def getHeight(self) :
      # Find the maximum y value in the polygon -- that's the height.
      my = self._points[0][1]
      for i in range(len(self._points)) :
          if self._points[i][1] > my :
              my = self._points[i][1]
      return my

   # Overrides the superclass method to draw the polygon.
   def draw(self, canvas) :
      super().draw(canvas)
      last = len(self._points) - 1
      for i in range(last) :
         start = self._points[i]
         end = self._points[i + 1]
         canvas.drawLine(self._x + start[0], self._y + start[1], \
                          self._x + end[0], self._y + end[1])
      start = self._points[last]
      end = self._points[0]
      canvas.drawLine(self._x + start[0], self._y + start[1], \
                       self._x + end[0], self._y + end[1])



if __name__ == "__main__" :
    win = graphics.GraphicsWindow()
    canvas = win.canvas()
    poly = Polygon([[200,100],[100,300],[300,300]])
    print("Height:", poly.getHeight())
    print("Width:", poly.getWidth())
    poly.draw(canvas)
    win.wait()