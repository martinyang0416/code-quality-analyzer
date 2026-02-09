n = int(input())
collection = set()

for _ in range(n):
    op = input().split()
    if op[0] == '+':
        v = int(op[1])
        collection.add(v)
    elif op[0] == '-':
        v = int(op[1])
        collection.discard(v)
    elif op[0] == '?':
        p = op[1]
        x = int(p, 2)
        print(1 if x in collection else 0)