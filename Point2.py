"""
1) Update the class Point in order to give the possibility to create a Point with either 0 or 2 arguments
Ex:
    p=Point()
    print(p) # <0,0>
    p=Point(2,3)
    print(p) # <2,3>

2) Update the methods __add__() in order to give the possibility to add a Point with Point but also a Point with an int
    
3) Add a method clear(): it's purpose is to reset the coordinates of a Point to 0:
    p=Point(2,3)
    print(p) # <2,3>
    p.clear()
    print(p) # <0,0>

"""

import math

class Point: 
    # __new__(), __init__(), __repr__(), __eq__()
    def __init__(self, valx, valy): # the constructor
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    
p1=Point(1,2)

# 1) p1=Point.__new__()
# 2) p1.__init__(1,2)
# 3) __init__(p1,1,2)

print(p1) # <1,2>

# 1) print(str(p1))
# 2) print(p1.__repr__())
# 3) print(__repr__(p1))

print(p1.x) # 1
print(p1.y) # 2
p1.x=4
print(p1) # <4,2>

p2=Point(0,3)
print(p2) # <0,3>

p3=p1+p2
# 1) p3=p1.__add__(p2)
# 2) p3=__add__(p1, p2)

print(p3) # <4,5>

result=p1.distance(p2)
print(f"Distance between {p1} and {p2} is {result}")
print(p1)
p2.x=4
p2.y=5
print(p2)
if p1 == p2:
#if p1.__eq__(p2):
    print("Equal")
else:
    print("Different")

