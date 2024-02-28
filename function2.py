
def third(arg1):
    if isinstance(arg1, (int,float)):
        temp=arg1**2 # temp is a "local" variable
        return temp
    else:
        print("Wrong argument received")

data=[0]*10

# result=third(12)
# print(result)
# result=third(arg1=12)
# print(result)