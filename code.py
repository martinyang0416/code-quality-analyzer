n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

for k in range(1, m + 1):
    for i in range(n - 1):
        if t[i] % k > t[i+1] % k:
            t[i], t[i+1] = t[i+1], t[i]

for number in t:
    print(number)