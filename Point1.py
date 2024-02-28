class Point: # __new__(), __init__(), __repr__()

    def __init__(self, valx, valy):
        self.x=valx
        self.y=valy
    def __repr__(self):
        return f"<{self.x},{self.y}>"

p1=Point(1,2)
# 1) p1=Point.__new__()
# 2) p1.__init__(1,2)
# 3) __init__(p1,1,2)

print(p1) # <1,2>
# 1) print(str(p1))
# 2) print(p1.__repr__())
# 3) print(__repr__(p1))

print(p1.x) # 1
p1.x=4
print(p1) # <4,2>

p2=Point(0,3)
print(p2) # <0,3>

p3=p1+p2
print(p3) # <4,5>

result=p1.distance(p2)

if p1 == p2:
    print("Equal")
else:
    print("Different")

