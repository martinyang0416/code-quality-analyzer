MOD = 998244353

def main():
    import sys
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    
    # Precompute factorial and inverse factorial up to n
    max_n = n
    fact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i-1] * i % MOD
    
    inv_fact = [1] * (max_n + 1)
    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
    for i in range(max_n - 1, -1, -1):
        inv_fact[i] = inv_fact[i+1]