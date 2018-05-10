#
# This Project Just Show a Way to code Sin(), Cos(), and Exp()
# Using Boork Taylor's work on polynomial functions
#
# Created by Louis Lamalle and Quentin Dieppe
#

from exponential import *

def cosinus(x, precision):
    cos0 = 1
    res = cos0
    n = -1

    for i in range(precision):
        if i % 2 == 1:
           if n == -1:
                res = res + (n * power(x, i + 1)) / factorial(i + 1)
                n = 1
           else :
                if n == 1 :
                    res = res + (n * power(x, i + 1)) / factorial(i + 1)
                    n = -1
    return (res)


if __name__ == '__main__' :
    print(cosinus(0, 100))
    print(cosinus(0.4, 100))
    print(cosinus(1.1, 100))
    print(cosinus(3.14, 100))
    print(cosinus(30, 100))
