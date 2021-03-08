# Math library
# use the .listFeatures() to get a table of all functions and constants
# Created by Arjun Sarao
import decimal
#===============================================================================
def pi( prec = 10 ** 1 ):
    decimal.getcontext().prec = prec
    b =  decimal.Decimal(1)
    pi = 0
    for k in range(prec):
        pi += ( b*4/(8*k+1) - b*2/(8*k+4) - b*1/(8*k+5) - b*1/(8*k+6)) / 16**k
    return pi
# Also some formula I found on the internet lmao
#===============================================================================
def eulersNumber():
    e = (1+(1/10000))**10000
    # print(e)
    return e
# Uses e = lim x-> inf (1+(1/x))^x
#===============================================================================
def goldenRatio():
    phi = (1 + roots(2, 5)) / 2
    return phi
#===============================================================================
def goldenRatioInv():
    phiInv = (1 - roots(2, 5)) / 2
    return phiInv
#===============================================================================
def logarithims(b, x):
    ans = naturalLog(x) / naturalLog(b)
    return ans
# Uses logb(x) = ln(x) / ln(b)
#===============================================================================
def naturalLog(x):
    ln = 10000 * (x)**(1/10000) - 10000
    return ln
# Some formula I found online
#===============================================================================
def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        print("Cannot take factorial of numbers less than 1.")
    elif n == 0:
        print("The value of 0! is: 1")
    else:
        return n * factorial(n - 1)
    print("The value of ", n, "! factorial is: ", int(factorial(n)))
# Recursively generates factorial
#===============================================================================
def powers(a, x):
    ans = eulersNumber() ** (a * naturalLog(x))
    return ans
# Uses a^x = e^(x*ln(a))
#===============================================================================
def roots(a, x):
    ans = eulersNumber() ** ((1 / a) * naturalLog(x))
    return ans
# Uses a^x = e^((1/x)*ln(a))
#===============================================================================
def permutations(n, r):
    perms = factorial(n) / factorial(n-r)
    return perms
#===============================================================================
def combinations(n, r):
    perms = factorial(n) / (factorial(r) * factorial(n-r))
    return perms
#===============================================================================
def fibonacci(n):
    number = ((goldenRatio()**n) - ((goldenRatioInv())**n))/ roots(2,5)
    return number
#===============================================================================
def circleArea(r):
    area = pi() * powers(r, 2)
#===============================================================================
def listFunctions():
    print("> Calculates constants such as pi, e, and phi.")
    print("> Can take logarithims of variable bases.")
    print("> Calculate number of permutations and combinations")
    print("> Returns the number at a specified index of a fibonacci series.")
    print("> Calculates the factorial of a number")
    print("> Can find the roots or powers of any numbers")
