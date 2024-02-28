
def first():
    print("Hello I'm function first")

first()
first()
result=first()
print(result)

def second(arg1=10):
    #if isinstance(arg1, int):
    if isinstance(arg1, (int,float)):
        print("Hello I'm function second")
        print("The argument is", arg1)
    else:
        print("Wrong argument received")

second(13.34)
second("abc")
second()
result=second()
print(result)