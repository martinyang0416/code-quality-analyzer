def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    m = int(input[ptr])
    ptr += 1
    s = int(input[ptr])
    ptr += 1
    size = 1 << m  # 2^m
    g = list(map(int, input[ptr:ptr+size]))
    ptr += size
    
    # Function to compute the average with 6 decimal places
    def compute_avg():
        total = sum(g)
        avg = total / size
        return "{0:.6f}".format(avg)
    
    # Print initial average
    print(compute_avg())
    
    for _ in range(s):
    