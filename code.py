from collections import deque
import sys

def main():
    w, h = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for _ in range(h)]
    
    # Find the starting position of 'R'
    start = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'R':
                start = (i, j)
                break
        if start:
            break
    
    # Calculate total number of floor cells (including 'R')
    total_floor = 0
    for i 