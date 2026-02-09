def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    numbers = list(map(int, input[1:n+1]))
    
    counts = [0, 0, 0]
    for num in numbers:
        mod = num % 3
        counts[mod] += 1
    
    c0, c1, c2 = counts
    total = 0
    
    # Triplets from each individual group
    if c0 >= 3:
        total += c0 * (c0 - 1) * (c0 - 2) // 6
    if c1 >= 3:
        total += c1 * (c1 - 1) * (c1 - 2) // 6
    if c2 >= 3:
        total += c2 * (c2 - 1) * (c2 - 2