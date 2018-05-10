#
# This Project Just Show a Way to code Sin(), Cos(), and Exp()
# Using Brook Taylor's work on polynomial functions
#
# Created by Louis Lamalle and Quentin Dieppe
#

from fractions import Fraction

def power(x, p):
    m = x
    i = 1

    while i < p :
       x = x * m
       i = i + 1
    return (x)

def factorial(n):
    i = 1
    x = 1

    if n < 0 :
       return 0

    while i < n + 1:
        x = x * i
        i = i + 1
    return (x)

def exponential(x, precision):
    exp0 = 1
    res = exp0
    i = 0

    for i in range(precision):
        res = res + (exp0 * power(x, i + 1)) / factorial(i + 1)
    return (res)

if __name__ == '__main__' :
    print(exponential(5, 150))
    print(exponential(22, 150))
    print(exponential(100, 800))
