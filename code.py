def count_trimensional_coordinates(n, a, b, c):
    l1 = a + 1
    r1 = a + n
    l2 = b + 1
    r2 = b + n
    l3 = c + 1
    r3 = c + n

    lower = max(l1, l2, l3)
    upper = min(r1, r2, r3)

    if lower > upper:
        return 0
    else:
        return upper - lower + 1

# Read input
n, a, b, c = map(int, input().split())
print(count_trimensional_coordinates(n, a, b, c))