def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    Y = int(data[1])
    G = list(map(int, data[2:2+N]))
    
    # Transform the array
    A = [g - Y for g in G]
    
    # Compute prefix sums
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]
    
    # Collect all prefix sums and sort them
    prefix_sums = prefix.copy()
    sorted_prefix = sorted(prefix_sums)
    
    # Assign ranks
    r