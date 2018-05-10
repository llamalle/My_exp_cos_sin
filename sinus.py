#
# This Project Just Show a Way to code Sin(), Cos(), and Exp()
# Using Boork Taylor's work on polynomial functions
#
# Created by Louis Lamalle and Quentin Dieppe
#

from exponential import *

def sinus(x, precision):
    sin0 = 0
    res = sin0
    n = 1

    for i in range(precision):
        if i % 2 == 0:
            res = res + (n * power(x, i + 1)) / factorial(i + 1)
            n = n * -1
    return (res)


if __name__ == '__main__' :
    print(sinus(0, 100))
    print(sinus(0.4, 100))
    print(sinus(1.1, 100))
    print(sinus(3.14, 100))
    print(sinus(30, 100))
