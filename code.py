def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        c = list(map(int, input[ptr:ptr+N]))
        ptr += N
        S = sum(c)
        if S % N != 0:
            print(-1)
            continue
        avg = S // N
        running = 0
        transfers = 0
        for i in range(N):
            running += c[i] - avg
            if i != N - 1:
                trans