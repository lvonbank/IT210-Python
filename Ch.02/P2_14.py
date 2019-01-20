# Levi VonBank

## Reads a number between 1,000 and 999,999 from the user and 
# prints it with a comma separating the thousands.

n = int(input("Enter a number between 1000 and 999999: ")) 
thousands = n / 1000
remainder = n % 1000
print("%d,%d" % (thousands, remainder))