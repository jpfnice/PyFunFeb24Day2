
def myfct(**arguments):
    print(arguments)

result=myfct()
print(result)
result=myfct(a=12)
print(result)
result=myfct(a=12,b=34,file="data.txt")
print(result)
