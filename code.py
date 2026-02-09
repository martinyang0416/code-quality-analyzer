m = int(input())
chapters = []
for _ in range(m):
    start, end = map(int, input().split())
    chapters.append(end)
p = int(input())

count = 0
for end in chapters:
    if end <= p:
        count += 1
    else:
        break
print(count)