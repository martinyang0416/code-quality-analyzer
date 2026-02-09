n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

min_row = n
max_row = -1
min_col = m
max_col = -1
has_sample = False

for i in range(n):
    for j in range(m):
        if grid[i][j] == 's':
            has_sample = True
            min_row = min(min_row, i)
            max_row = max(max_row, i)
            min_col = min(min_col, j)
            max_col = max(max_col, j)

if not has_sample:
    for row in grid:
        print(''.join(row))
    exit()

# Now, mark 