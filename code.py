def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        ranges = []
        for _ in range(N):
            S = int(input[ptr])
            E = int(input[ptr + 1])
            ranges.append((S, E))
            ptr += 2
        scores = [0] * N
        for i in range(N):
            for j in range(i + 1, N):
                s_i, e_i = ranges[i]
                s_j, e