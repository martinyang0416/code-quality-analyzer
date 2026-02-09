import sys

def compute_spf(max_y):
    spf = [0] * (max_y + 1)
    spf[1] = 1
    for i in range(2, max_y + 1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i*i, max_y + 1, i):
                if spf[j] == 0:
                    spf[j] = i
    # Handle cases where spf is still 0 (which shouldn't happen except for 1)
    # However, double-checking all numbers
    for i in range(2, max_y + 1):
        if spf[i] == 0:
            spf[i] = i
    return spf

def main():
