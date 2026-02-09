def main():
    import sys
    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    for _ in range(T):
        S = input[index]
        index += 1
        flips = 0
        res = 0
        for c in S:
            val = int(c)
            actual = val ^ (flips % 2)
            if actual == 1:
                res += 1
                flips += 1
        print(res)

if __name__ == "__main__":
    main()