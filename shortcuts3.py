
text="12:34:56:67"
result=text.split(":")
print(result)

# newlist=[]
# for e in result:
#     newlist.append(int(e))

# print(newlist, sum(newlist))

# list comprehension:
# newlist=[int(e) for e in result]
# print(newlist, sum(newlist))

newlist=list(map(int,result))
print(newlist)