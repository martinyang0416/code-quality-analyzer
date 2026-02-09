t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [1 if x == 0 else 0 for x in b]
    print(' '.join(map(str, a)))