# This program contains functions that evaluate formulas used in geometry.
#
# Olivia Schreiner
# August 30, 2017

import math

def triangle_area(b,h):
    a = (1/2) * b * h
    return a

def circle_area(r):
    a = math.pi * r**2
    return a

def parallelogram_area(b,h):
    a = b * h
    return a

def trapezoid_area(c,b,h):
    a = ((c + b) / 2) * h
    return a

def rect_prism_volume(w,h,l):
    v = w * h * l
    return v

def cone_volume(r,h):
    v = math.pi * r**2 * (h / 3)
    return v

def sphere_volume(r):
    v = (4/3) * math.pi * r**3
    return v

def rect_prism_sa(w,h,l):
    a = 2 * (w * l + h * l + h * w)
    return a

def sphere_sa(r):
    a = 4 * math.pi * r**2
    return a

def hypotenuse(w,x,y,z):
    d = math.sqrt(((y - w)**2) + ((z - x)**2))
    return d
def herons_formula(b,c,d):
    s = (b + c + d)/2
    a = math.sqrt(s * (s - b) * (s - c) * (s- d))
    return a

#function calls
print(triangle_area(4,9))
print(circle_area(5))
print(circle_area(12))
print(parallelogram_area(2,2))
print(trapezoid_area(1,2,3))
print(rect_prism_volume(1,2,3))
print(cone_volume(2,3))
print(sphere_volume(2))
print(rect_prism_sa(2,2,2))
print(sphere_sa(2))
print(hypotenuse(1,2,3,4))
print(herons_formula(3,5,7))
