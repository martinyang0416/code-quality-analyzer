def main():
    import sys
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))
    visited = [False] * n
    cycle_count = 0

    for i in range(n):
        if not visited[i]:
            cycle_count += 1
            current = i
            while not visited[current]:
                visited[current] = True
                next_pos = p[current] - 1
                current = next_pos

    print(n - cycle_count)

if __name__ == "__main__":
    main()