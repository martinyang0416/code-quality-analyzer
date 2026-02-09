import sys

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        n = int(input[idx])
        idx +=1
        s = input[idx]
        idx +=1
        positions = []
        for i, c in enumerate(s):
            if c == '#':
                positions.append(i)
        k = len(positions)
        if k <= 1:
            print(0)
            continue
        # Compute q_i = positions[i] - i
        q = [positions