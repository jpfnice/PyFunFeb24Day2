import functools

data=[1,2,34,-20,45,67,10,-30]

def mulTen(arg):
    return arg*10

newlist=list(map(mulTen, data))
print(newlist)

def myFilter(arg):
    return arg > 0

newlist=list(filter(myFilter, data))
print(newlist)

def isEven(arg):
    return arg % 2 == 0

newlist=list(filter(isEven, data))
print(newlist)

def mult(a, b):
    return a*b

result=functools.reduce(mult, data)
print(result)

