# Levi VonBank

# Imports sqrt and pi from math module
from math import sqrt
from math import pi

def main():
    r1 = input("Please input the smallest radius: ")
    r2 = input("Please input the largest radius: ")
    h = input("Please input the height: ")
    if r1 != "" and r2 != "" and h != "":
        r1 = float(r1)
        r2 = float(r2)
        h = float(h)
        v = volume(r1,r2,h)
        s = surfaceArea(r1,r2,h)
        print("The volume is %.2f and surface area is %.2f" % (v,s))
    else:
        print("Missing input")

## Find the volume of a frustum of a cone
# @parm r1 takes the smallest radius and plugs it into the formula
# @parm r2 takes the largest radius and plugs it into the formula
# @parm h takes the height and plugs it into the formula
# @return send back volume
def volume(r1,r2,h):
    v = ((1/3)*(pi)*(h)) * ((r1**2)+(r2**2)+(r1*r2))
    return v

## Find the surface area of a frustum of a cone
# @parm r1 takes the smallest radius and plugs it into the formula
# @parm r2 takes the largest radius and plugs it into the formula
# @parm h takes the heightand plugs it into the formula
# @return send back surface area
def surfaceArea(r1,r2,h):
    s = (pi*(r1+r2)) * sqrt(((r2-r1)**2)+(h**2))+(pi*(r1**2))
    return s

main()