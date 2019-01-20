# Levi VonBank

# Imports pi and sqrt for calculations
from math import pi
from math import sqrt

## Calculates sphere volume
# @r obtains radius
# @return volume of sphere
def sphereVolume(r):
    vol = 0
    try:
        r = float(r)
        if r > 0:
            vol = 4/3*pi*r**3
            return round(vol,2)
        else: return vol
    except:
        return vol

## Calculates sphere surface
# @r obtains radius
# @return surface of sphere
def sphereSurface(r):
    surf = 0
    try:
        r = float(r)
        if r > 0:
            surf = 4*pi*r**2
            return round(surf,2)
        else: return surf
    except:
        return surf

## Calculates cylinder volume
# @r obtains radius
# @h obtains height
# @return volume of cylinder
def cylinderVolume(r, h):
    vol = 0
    try:
        r = float(r)
        h = float(h) 
        if r > 0 and h > 0:
            vol = pi*r**2*h
            return round(vol,2)
        else: return vol
    except:
        return vol

## Calculates cylinder surface
# @r obtains radius
# @h obtains height
# @return surface of cylinder
def cylinderSurface(r, h):
    surf = 0
    try:
        r = float(r)
        h = float(h)         
        if r > 0 and h > 0:
            surf = 2*pi*r*h+2*pi*r**2
            return round(surf,2)
        else: return surf
    except:
        return surf

## Calculates cone volume
# @r obtains radius
# @h obtains height
# @return volume of cone
def coneVolume(r, h):
    vol = 0
    try:
        r = float(r)
        h = float(h)
        if r > 0 and h > 0:
            vol = pi*r**2*h/3
            return round(vol,2)
        else: return vol
    except:
        return vol

## Calculates cone surface
# @r obtains radius
# @h obtains height
# @return surface of cone
def coneSurface(r, h):
    surf = 0
    try:
        r = float(r)
        h = float(h)
        if r > 0 and h > 0:
            surf = pi*r*(r+sqrt(h**2+r**2))
            return round(surf,2)
        else: return surf
    except:
        return surf
    