import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    for _ in range(n):
        p = int(input[idx])
        q = int(input[idx+1])
        m = int(input[idx+2])
        idx += 3
        
        B = m
        numerator = (m - 1) + B * q
        denominator = p - 1
        a = (numerator + denominator - 1) // denominator
        total = a + B
        print(total)
        
if __name__ == "__main__":
    main()