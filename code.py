import bisect

n, m = map(int, input().split())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

stalls = [x[i] for i in range(len(f)) if f[i] == 1]
counts = [0] * len(stalls)

for i in range(len(x)):
    if f[i] == 0:
        x_c = x[i]
        pos = bisect.bisect_left(stalls, x_c)
        if pos == 0:
            counts[0] += 1
        elif pos == len(stalls):
            counts[-1] += 1
        else:
            d_left = x_c - stalls[pos-1]
            d_right = stalls