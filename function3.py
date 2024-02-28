
def mysum(*arguments):
    total=0
    for e in arguments:
        total += e
    return total

result=mysum()
print(result)
result=mysum(12)
print(result)
result=mysum(12,34,45)
print(result)
result=mysum(12,34,45,10,15)
print(result)