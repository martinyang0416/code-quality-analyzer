import sys

def main():
    n = int(sys.stdin.readline())
    S = (1200000) ** 2  # 1.2e6 squared is 1440000000000

    x, y = 0, 0
    result = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        tentative_x = x + a
        tentative_y = y + b
        dist_sq = tentative_x ** 2 + tentative_y ** 2
        if dist_sq <= S:
            x, y = tentative_x, tentative_y
            result.append('1')
        else:
            result.append('0')
    
    print(' '.