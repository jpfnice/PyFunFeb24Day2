
data=list(range(10)) # 0, 1, 2, 3, .. 9
print(data)

data=tuple(range(10)) # 0, 1, 2, 3, .. 9
print(data)

data=list(range(5,13)) # 5, .. 12
print(data)

data=list(range(1,20,2)) # 1,3,5,...19
print(data)

data=["first",3.4, 5.6, 7.8, True, False, "last"]

index=2
while index < len(data):
    print(index, "=>", data[index])
    index += 1
    
for element in data:
    print(element)
    
for index in range(2,len(data)):
    print(index, "=>", data[index])