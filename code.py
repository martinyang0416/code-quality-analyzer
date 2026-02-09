W, H = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

perimeter = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == 1:
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    perimeter += 1
                else:
                    if grid[ni][nj] == 0:
                       