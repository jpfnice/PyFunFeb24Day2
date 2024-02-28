"""
1) Update the class Point in order to give the possibility to create a Point with either 0 or 2 arguments
Ex:
    p=Point()
    print(p) # <0,0>
    p=Point(2,3)
    print(p) # <2,3>

2) Update the methods __add__() in order to give the possibility to add a Point with a Point but also a Point with an int
    
3) Add a method clear(): it's purpose is to reset the coordinates of a Point to 0:
    p=Point(2,3)
    print(p) # <2,3>
    p.clear()
    print(p) # <0,0>

"""

import math

class Point: 
    # __new__(), __init__(), __repr__(), __eq__()
    def __init__(self, *values): # the constructor
        if len(values) == 2:
            self.x=values[0]
            self.y=values[1]
        elif len(values) == 0:
            self.x=0
            self.y=0
        else:
            print("Wrong number of arguments received!")
            self.x=0
            self.y=0
            # A better strategy will be to raise an Exception !!
            
    def __repr__(self):
        return f"<{self.x},{self.y}>"
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x+other.x, self.y+other.y)
        elif isinstance(other, int):
            return Point(self.x+other, self.y+other)
        else:
            print("Wrong kind of arguments received!")
            return self
            # A better strategy will be to raise an Exception !!
            
    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)
    
    def clear(self):
        self.x=0
        self.y=0
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 
    
p1=Point(1,2)
print(p1) # <1,2>
p2=p1
print(p2) # <1,2>
p2.x=45
print(p2)
print(p1)
print(id(p1), id(p2))

import copy
p2=copy.copy(p1)

print(p2) # <1,2>
p2.x=100
print(p2)
print(p1)
print(id(p1), id(p2))


l1=[3,4]
l2=l1
l2.append(10)
print(id(l1), id(l2))
l2=l1.copy()
l2.append(30)
print(l1)
print(l2)
print(id(l1), id(l2))

l1=[23,45]
l2=l1
del l1
del l2

