import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    k = int(data[idx + 1])
    idx += 2
    
    e = list(map(int, data[idx:idx + n]))
    idx += n
    
    conflicts = [[] for _ in range(n)]
    for _ in range(k):
        x = int(data[idx]) - 1
        y = int(data[idx + 1]) - 1
        idx += 2
        conflicts[x].append(y)
        conflicts[y].append(x)
    
    sorted_e = sorted(e)
    result = [0] * n
 