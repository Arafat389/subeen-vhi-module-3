

def euclid_gcd(a,b):
    if b == 0:
        return a
    return euclid_gcd(b,a%b)
gcd = euclid_gcd(7,35)
print(gcd)

import sys
print(sys.getrecursionlimit())


import math
print(math.gcd(7,35))


def fun (n1,n2):
    print("receive",n1,n2)
    def is_even(n):
        if n%2 == 0:
            return True
        return False
    print(n1 ,is_even(n1))
    print(n2 ,is_even(n2))
fun(10,11)    