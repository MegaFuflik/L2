from decimal import *
from math import factorial
 
n=int(input())
n=n+1
def pi(n):
    Pi = Decimal(0)
    m = 0
    while m < n:
        Pi += (Decimal(-1)**m) * (Decimal(factorial(6 * m)) / ((factorial(m)**3) * (factorial(3 * m))) * (13591409 + 545140134 * m) / (640320**(3 * m)))
        m += 1
    Pi = Pi * Decimal(10005).sqrt() / 4270934400
    Pi = Pi**(-1)
    return Pi
 
 

getcontext().prec = n
print(pi(n))
