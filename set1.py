"""
Set: a kind of collection

"""

s1={3,4,5,10,-3,4, 10}
print(s1)

for e in s1:
    print(e)
print(len(s1))

s1=set([23,45,67,78,23])
print(s1)

s1.add(100)
print(s1)

s2={67,78,200,220}
print(s2)
s3=s1.union(s2)
print(s3)

s3=s1.intersection(s2)
print(s3)