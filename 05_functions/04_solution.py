import math

def circle_stats(radius):
    print("hi")
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_stats(3)

print("Area: ", round(a,2), "Circumference: ", round(c,2))
 