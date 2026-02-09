import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N % 2 == 0:
            res = N // 2
        else:
            res = (N - 1) // 2 + 1
        results.append(res)
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()