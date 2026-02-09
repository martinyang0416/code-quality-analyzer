n = int(input())
a = list(map(int, input().split()))
min_shots = float('inf')

for i in range(n - 2):
    left = a[i]
    mid = a[i + 1]
    right = a[i + 2]
    required = max(left, right, (mid + 2) // 3)
    if required < min_shots:
        min_shots = required

print(min_shots)