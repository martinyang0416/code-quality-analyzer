n = int(input())
h = list(map(int, input().split()))
if n == 0:
    print(0)
    exit()

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    j = i
    while j > 0 and h[j-1] == h[i]:
        j -= 1
    option1 = dp[i-1] + 1
    if j == 0:
        option2 = 1
    else:
        option2 = dp[j-1] + 1 if j > 0 else 1
    dp[i] = min(option1, option2)

print(dp[-1])