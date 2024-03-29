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

p4=Point()
print(p4)

p5=p4+6
print(p5)

p5.clear()
print(p5)