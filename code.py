def count_divisors(x):
    if x == 1:
        return 1
    count = 1
    i = 2
    while i * i <= x:
        exponent = 0
        while x % i == 0:
            exponent += 1
            x = x // i
        if exponent > 0:
            count *= (exponent + 1)
        i += 1
    if x > 1:
        count *= 2
    return count

n = int(input())
lst = list(map(int, input().split()))
counts = [count_divisors(x) for x in lst]

from collections import defaultdict
freq = defaultdict(int)
for c in counts:
 