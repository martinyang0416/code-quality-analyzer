import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().split())
    adj = [set() for _ in range(n)]
    for _ in range(k):
        parts = sys.stdin.readline().split()
        if not parts:
            continue
        if parts[0] == "CONNECT":
            u = int(parts[1])
            v = int(parts[2])
            adj[u].add(v)
            adj[v].add(u)
        elif parts[0] == "DISCONNECT":
            u = int(parts[1])
            v = int(parts[2])
    