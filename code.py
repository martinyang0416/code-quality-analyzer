def count_factors(n, factor):
    count = 0
    if n == 0:
        return 0
    while n % factor == 0:
        count += 1
        n = n // factor
    return count

def main():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        x = int(input[idx])
        y = int(input[idx + 1])
        idx += 2
        
        if x == 0 or y == 0:
            print(0, 0)
            continue
        
        a = count_factors(x, 2)
        b = co