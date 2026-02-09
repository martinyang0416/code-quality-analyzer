n = int(input())
stores_masks = []
for _ in range(n):
    bits = list(map(int, input().split()))
    mask = 0
    for i in range(10):
        if bits[i] == 1:
            mask += (1 << i)
    stores_masks.append(mask)

profits = []
for _ in range(n):
    profits.append(list(map(int, input().split())))

max_total = -float('inf')
for j_mask in range(1, 1 << 10):
    total = 0
    for i in range(n):
        store_mask = stores_masks[i]
        overlap = bin(j_mask & store_mask).count('1')
        t