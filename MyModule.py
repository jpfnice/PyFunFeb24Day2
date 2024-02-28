
def isPrime(number):
    """
    The purpose of the function isPrime is to determine if the number it receives as argument is a prime number or not.

    Parameters
    ----------
    number : int
        The number to be tested by isPrime

    Returns
    -------
    bool
        Returns True if number is a prime number

    """
    if isinstance(number, int):        
        if number > 1:
            divisor=2
            while divisor < number:
                if number % divisor == 0:
                    return False
                divisor = divisor + 1
            
            return True
        else:
            return False
    else:
        return False    # In this case a better option is to raise
                        # an exception (this will be covered later)