import math

def find_rectangle(n, m, x, y, A):
    best_rect = None
    best_distance_sq = float('inf')

    def get_divisors(a):
        divisors = []
        for d in range(1, int(math.isqrt(a)) + 1):
            if a % d == 0:
                divisors.append((d, a // d))
                if d != a // d:
                    divisors.append((a // d, d))
        return divisors

    divisors = get_divisors(A)

    for w, h in divisors:
        if w > n or h > m:
            new_w, new_h = h, w
 