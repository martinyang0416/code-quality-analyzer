M = int(input())
scores = list(map(int, input().split()))

sum_suffix = [0] * M
min_suffix = [0] * M

sum_suffix[-1] = scores[-1]
min_suffix[-1] = scores[-1]

for i in range(M-2, -1, -1):
    sum_suffix[i] = sum_suffix[i+1] + scores[i]
    min_suffix[i] = min(scores[i], min_suffix[i+1])

max_avg = -1
best_P = []

for P in range(M):
    n = M - P
    if n < 2:
        continue  # Not enough scores to drop one and average the rest
    total = sum_suffix[P] - min_suffix[P]
    avg = total / (n - 1)