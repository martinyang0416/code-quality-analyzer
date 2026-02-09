import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    M = int(input[idx])
    idx += 1
    
    T = []
    for _ in range(N):
        T.append(int(input[idx]))
        idx += 1
    
    adj = [[] for _ in range(N)]
    in_degree = [0] * N
    deps = [[] for _ in range(N)]
    
    for _ in range(M):
        A = int(input[idx]) - 1
        idx += 1
        B = int(input[idx]) - 1
        idx += 1
        
  