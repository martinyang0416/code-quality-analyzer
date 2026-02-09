import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    digits = [sys.stdin.readline().strip() for _ in range(n)]

    # Define the masks for each digit (0-9) as binary strings
    digit_masks = [
        '1111110',  # 0
        '0110000',  # 1
        '1101101',  # 2
        '1111001',  # 3
        '0110011',  # 4
        '1011011',  # 5
        '1011111',  # 6
        '1110000',  # 7
        '1111111',  # 8
        '1111011',  # 9
    ]

    # Precompute for each digit th