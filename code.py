import sys

def main():
    m, r = map(int, sys.stdin.readline().split())
    pages = list(map(int, sys.stdin.readline().split()))
    weights = list(map(int, sys.stdin.readline().split()))
    
    # Calculate the delta for each book: delta = weight - r * pages
    dp = {0: 0}  # key: current delta, value: max weight for this delta
    
    for p, w in zip(pages, weights):
        delta_i = w - r * p
        temp = {}
        # Iterate through existing deltas in dp
        for current_d in dp:
