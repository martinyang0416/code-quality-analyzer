def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    Q_num = int(input[idx])
    idx += 1
    
    P = list(map(int, input[idx:idx+N]))
    idx += N
    
    Q = list(map(int, input[idx:idx+N]))
    idx += N
    
    # Compute prefix sums
    prefix = [0] * (N + 1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + P[i-1] * Q[i-1]
    
    for _ in range(Q_num):
        L = int(input[idx])
        idx +=1
        R = int(