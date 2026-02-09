import sys

def count_a_in_hex_range(x, y):
    start = min(x, y)
    end = max(x, y)
    total = 0
    for n in range(start, end + 1):
        hex_str = hex(n)[2:]  # Get the hex without '0x'
        # Convert to uppercase to count 'A's
        total += hex_str.upper().count('A')
    return total

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    N = int(input[idx])
    idx += 1
    for _ in range(N):
        x = int(input[idx])
        y = int(input[idx+1])
      