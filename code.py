import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0

    m = int(input[ptr])
    ptr += 1

    if m == 1:
        # Only root node, but m >=2 per problem statement
        pass
    else:
        p = list(map(int, input[ptr:ptr + (m - 1)]))
        ptr += (m - 1)

    # Build adjacency list
    adj = [[] for _ in range(m + 1)]
    for i in range(2, m + 1):
        parent = p[i - 2]
        adj[i].append(parent)
        adj[parent].append(i)

    