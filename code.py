def main():
    import sys
    n = int(sys.stdin.readline())
    blocks = []
    for _ in range(n):
        a, b, v = map(int, sys.stdin.readline().split())
        blocks.append((a, b, v))
    
    dp = [0] * 5  # indexes 1-4 used
    for a, b, v in blocks:
        before_dp = dp.copy()
        temp_dp = before_dp.copy()
        for s, e in [(a, b), (b, a)]:
            if before_dp[s] + v > temp_dp[e]:
                temp_dp[e] = before_dp[s] + v
        dp = temp_dp.copy()
    
    print(max