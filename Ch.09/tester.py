# Levi VonBank
# P9_14 Tester

from P9_14 import *

r = input("Enter a radius: ")
h = input("Enter a height: ")

print()
print("sphereVolume:", sphereVolume(r))
print("sphereSurface:", sphereSurface(r))
print("cylinderVolume:", cylinderVolume(r, h))
print("cylinderSurface:", cylinderSurface(r, h))
print("coneVolume:", coneVolume(r, h))
print("coneSurface:", coneSurface(r, h))