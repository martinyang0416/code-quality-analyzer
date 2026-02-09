import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    h_list = []
    a_list = []
    for _ in range(n):
        h, a = map(int, sys.stdin.readline().split())
        h_list.append(h)
        a_list.append(a)
    
    h_count = defaultdict(int)
    for h in h_list:
        h_count[h] += 1
    
    for i in range(n):
        a_i = a_list[i]
        x = h_count.get(a_i, 0)
        home = (n - 1) + x
        away = (n - 1) - x
        print(f"{home} {away