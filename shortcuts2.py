
data=[12,34,-56,67,-34,-4]

# newlist=[]
# for e in data:
#     if e > 0:
#         newlist.append(e**2)

newlist=[e**2 for e in data if e > 0]
print(newlist)