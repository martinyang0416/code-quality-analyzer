t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (k + 1)
    dp[0] = 1
    for num in a:
        for s in range(k, num - 1, -1):
            dp[s] += dp[s - num]
    print(dp[k])