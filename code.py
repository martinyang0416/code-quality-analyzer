import sys

def main():
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        n = int(input[ptr])
        ptr += 1
        p = int(input[ptr])
        ptr += 1
        vertices_count = 4 * n
        edges = []
        for _e in range(p):
            u = int(input[ptr])
            ptr += 1
            v = int(input[ptr])
            ptr += 1
            edges.append((u, v, _e + 1))  # 1-based index for edges

        # Initialize gre