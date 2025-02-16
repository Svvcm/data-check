"""Dummy challenge for Kitt Demo"""

import math

def circle_area(radius):
    """Returns the area of the circle of given radius"""
    if radius < 0:
        return 0
    return round(math.pi * radius**2 , 2)
