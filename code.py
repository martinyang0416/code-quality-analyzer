n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
result = []

for s in range(2 * n - 1):
    i_min = max(0, s - (n - 1))
    i_max = min(s, n - 1)
    for i in range(i_min, i_max + 1):
        j = s - i
        result.append(str(a[i][j]))

print(' '.join(result))