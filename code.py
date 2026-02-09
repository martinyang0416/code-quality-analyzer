import sys

def main():
    N = int(sys.stdin.readline())
    for _ in range(N-1):
        sys.stdin.readline()  # read and ignore edges
    sys.stdin.readline()      # read and ignore colors
    print(N)

if __name__ == "__main__":
    main()