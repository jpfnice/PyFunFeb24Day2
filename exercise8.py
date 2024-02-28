"""
    Define a function addList() which purpose is to add 2 lists
    of numbers given as arguments, element by element.
    
    Example:
        l1=[5,6,3]
        l2=[1,0,-1,10]
        l3=addList(l1, l2) # l3 is [6,6,2,10]
        
"""

def addList(list1, list2):
    newList=[]
    if len(list1) > len(list2):
        for index in range(len(list2)): 
            newList.append(list1[index]+list2[index])
        for index in range(len(list2), len(list1)): 
            newList.append(list1[index])
    else:
        for index in range(len(list1)):
            newList.append(list1[index]+list2[index])
        for index in range(len(list1), len(list2)):
            newList.append(list2[index])
    return newList

def addList_version2(list1, list2):
    newList=[]
    # First I do extend the shortest list:
    if len(list1) > len(list2):
        list2.extend([0]*(len(list1)-len(list2)))
    else:
        list1.extend([0]*(len(list2)-len(list1)))
    # Now the 2 list are of the same size!
    for index in range(len(list1)):
        newList.append(list1[index]+list2[index])
    return newList

l1=[5,6,3]
l2=[1,0,-1,10]
l3=addList(l1, l2) # l3 is [6,6,2,10]
print(l3)
l3=addList_version2(l1, l2) # l3 is [6,6,2,10]
print(l3)

l1=[5,6,3,10,20]
l2=[1,11]
l3=addList(l1, l2) # l3 is [6,17,3,10,20]
print(l3)
l3=addList_version2(l1, l2) # l3 is [6,17,3,10,20]
print(l3)