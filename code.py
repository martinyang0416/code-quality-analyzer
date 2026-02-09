n, x, y = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

count = 0
for pages in p:
    required_x = (pages + 1) // 2
    if x >= required_x:
        x -= required_x
        count += 1
    else:
        if y >= pages:
            y -= pages
            count += 1
print(count)