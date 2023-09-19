# day 8 just plays around with functions.
import math
def isprime(number):
    for _ in range (2,int(math.sqrt(number))+1):
        if number % _ == 0:
            return (False)
        
    return (True)

print(isprime(11))