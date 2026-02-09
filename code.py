def count_valid_bs(L):
    count = 0
    d = 1
    while True:
        b = 10**d -1
        if b > L:
            break
        count +=1
        d +=1
    return count

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for _ in range(T):
        K = int(input[idx])
        L = int(input[idx+1])
        idx +=2
        count_b = count_valid_bs(L)
        if count_b ==0:
            print(0, 0)
        else:
            total_pairs