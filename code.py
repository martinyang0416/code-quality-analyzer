def main():
    import sys
    m, D = map(int, sys.stdin.readline().split())
    stations = []
    for idx in range(m):
        y, w = map(int, sys.stdin.readline().split())
        stations.append((y, w, idx + 1))  # store original index (1-based)
    
    # Sort stations by their position
    stations.sort()
    
    prev_time = 0
    prev_y = 0
    current_min_prev = 0  # min(DP[j] - y_j) up to previous stations
    selected = [False] * m
    
    for i in range(m):
        y, w, orig_idx = s