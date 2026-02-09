n = int(input())
islands = set()
for _ in range(n):
    x, y = map(int, input().split())
    islands.add((x, y))

total = 0

for x, y in islands:
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if (x + dx, y + dy) not in islands:
            total += 1

print(total)