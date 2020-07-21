import sys
import math
from decimal import *
from math import factorial
from time import time

# http://thelivingpearl.com/2013/05/28/computing-pi-with-python/
# http://www.numberworld.org/misc_runs/pi-5t/details.html

# Bellard's Formula PI

def bellard(n):
    pi = Decimal(0)
    k = 0
    while k < n:
      pi += (Decimal(-1)**k/(1024**k))*( Decimal(256)/(10*k+1) + Decimal(1)/(10*k+9) - Decimal(64)/(10*k+3) - Decimal(32)/(4*k+1) - Decimal(4)/(10*k+5) - Decimal(4)/(10*k+7) - Decimal(1)/(4*k+3))
      k += 1
    pi = pi * 1/(2**6)
    return pi

# Bailey-Borwein-Plouffe formula

def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return pi

# http://www.craig-wood.com/nick/articles/pi-chudnovsky/

def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

def chudnovsky2(n):
    pi = Decimal(13591409)
    ak = Decimal(1)
    k = 1
    while k < n:
        ak *= -Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k*k*k*26680*640320*640320)

        val = ak*(13591409 + 545140134*k)
        
        d = Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k*k*k*26680*640320*640320)
        
        pi += val
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi

# arctan
# http://www.craig-wood.com/nick/articles/pi-machin/

def arctan(x):
    """
    Calculate arctan(1/x)

    arctan(1/x) = 1/x - 1/3*x**3 + 1/5*x**5 - ... (x >= 1)

    This calculates it in fixed point, using the value for one passed in
    """
    x2 = x*x
    x = Decimal(x)

    total = Decimal(0)
    sign = 1
    for i in range(1, 512, 2):
        #total += sign / (i * x)
        total += sign / (i * x ** i)
        sign = -sign
        #x *= x2
        #print(total)
    return total

def pi_machin(n):
    return 4*(4*arctan(5) - arctan(239))

def pi_gauss(one):
    return 4*(12*arctan(18) + 8*arctan(57) - 5*arctan(239))

if __name__ == "__main__":
  
  N = 100000000
  
  getcontext().prec = N
  
  a = chudnovsky2(N)
  print(a)