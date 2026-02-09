def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        N = int(input[idx])
        idx +=1
        W = list(map(int, input[idx:idx+N]))
        idx +=N
        Y = int(input[idx])
        idx +=1
        
        fountains = []
        for i in range(N):
            t1 = i / Y
            t2 = (N - 1 - i)
            earliest = min(t1, t2)
            fountains.append((earliest, i, t1, t2))
        
        #