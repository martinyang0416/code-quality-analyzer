import math

def get_divisors(p):
    divisors = set()
    for i in range(1, int(math.isqrt(p)) + 1):
        if p % i == 0:
            divisors.add(i)
            divisors.add(p // i)
    return sorted(divisors)

def count_pairs(p, q):
    if p < q:
        return 0
    divisors = get_divisors(p)
    count = 0
    for d in divisors:
        if d < q:
            continue
        if p % d != 0:
            continue
        v = p // d
        if v < q:
            continue
        x = d - q
    