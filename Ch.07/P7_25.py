# Levi VonBank

##
#  This program processes a digital image by creating a negative of a BMP image.
#

from io import SEEK_CUR

def main() :
   filename = input("Please enter the file name: ")

   # Open as a binary file for reading and writing.
   imgFile = open(filename, "rb")
   newImgFile = open("lenaGrayscale.bmp", "wb")
   
   newImgFile.write(imgFile.read())
   
   imgFile.close()
   newImgFile.close()
   
   newImgFile = open("lenaGrayscale.bmp", "rb+")
   
   # Extract the image information.
   fileSize = readInt(newImgFile, 2)
   start = readInt(newImgFile, 10)
   width = readInt(newImgFile, 18)
   height = readInt(newImgFile, 22)

   # Scan lines must occupy multiples of four bytes.
   scanlineSize = width * 3
   if scanlineSize % 4 == 0 :
      padding = 0
   else :
      padding = 4 - scanlineSize % 4
      
   # Make sure this is a valid image.      
   if fileSize != (start + (scanlineSize + padding) * height) :
      exit("Not a 24-bit true color image file.")

   # Move to the first pixel in the image.
   newImgFile.seek(start)
   
   # Process the individual pixels.
   for row in range(height) :  # For each scan line
      for col in range(width) :  # For each pixel in the line
         processPixel(newImgFile)         

      # Skip the padding at the end
      newImgFile.seek(padding, SEEK_CUR)
      
   newImgFile.close()
   
   print("Done!")

## Processes an individual pixel.
#  @param imgFile the binary file containing the BMP image
#
def processPixel(imgFile) :
   # Read the pixel as individual bytes.
   theBytes = imgFile.read(3)
   blue = theBytes[0]
   green = theBytes[1]
   red = theBytes[2]

   # Process the pixel.
   grayscale = round(0.299*(red) + 0.587*(green) + 0.114*(blue))
   newBlue = grayscale
   newGreen = grayscale
   newRed = grayscale
   
   # Write the pixel.
   imgFile.seek(-3, SEEK_CUR)   # Go back 3 bytes to the start of the pixel
   imgFile.write(bytes([newBlue, newGreen, newRed])) 
           
## Gets an integer from a binary file.
#  @param imgFile the file
#  @param offset the offset at which to read the integer
#  @return the integer starting at the given offset
#
def readInt(imgFile, offset) :
   # Move the file pointer to the given byte within the file.
   imgFile.seek(offset)
      
   # Read the 4 individual bytes and build an integer.
   theBytes = imgFile.read(4)   
   result = 0
   base = 1
   for i in range(4) :
      result = result + theBytes[i] * base 
      base = base * 256
      
   return result

# Start the program.
main()
