import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        n, C = int(input[idx]), int(input[idx+1])
        idx +=2
        edges = [[] for _ in range(n+1)]
        degree = [0]*(n+1)
        for _ in range(n-1):
            v = int(input[idx])
            u = int(input[idx+1])
            c = int(input[idx+2])
            idx +=3
            edges[v].append(u)
            edges[u].ap