"""
    Define a function isPrime which purpose is to determine if
    the number it receives as argument is a prime number or not.
    
    Step1:
        test the argument received to ensure it is an int > 1
    Step2:
        with the help of a loop try to divide the argument received 
        (lets call it "number") by 2,3,4,5, up to number-1
        For instance, if number is 17 you can test: 2,3,4,5,...,15,16
        Ex: if number % 2 == 0 then 2 is a divisor of number
        As soon as you find a divisor of "number" you can return False
    Step3:
        At the end of the loop, you will have tested all possible
        divisor of number, you can return True: "number" is a 
        prime number
"""
   

def isPrime(number):
    # To be completed
    return True

tests=[-1,2,4,5,6,7,11,26,27,1233]

for e in tests:
    if isPrime(e):
        print(e, "is a prime number")
    else: 
        print(e,"is NOT a prime number")
