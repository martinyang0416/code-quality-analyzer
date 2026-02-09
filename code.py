t = int(input())
for _ in range(t):
    n = int(input())
    sequence = [1]
    current = 1
    max_power = 0
    while True:
        next_val = current * 3
        if next_val > n:
            break
        sequence.append(next_val)
        current = next_val
        max_power += 1
    print(max_power)
    print(' '.join(map(str, sequence)))