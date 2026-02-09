import sys
import math

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def crt(a1, m1, a2, m2):
    g, x, y = extended_gcd(m1, m2)
    if (a1 - a2) % g != 0:
        return None
    lcm = m1 // g * m2
    x0 = (a1 + (x * (a2 - a1) // g) % (m2 // g) * m1) % lcm
    return x0

def compute_same_days(d, r1, r2, n, m):
    same = 0
    for x in range(d):
        a = x % n
        b = x % m
   