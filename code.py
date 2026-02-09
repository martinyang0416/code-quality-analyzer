from collections import Counter

def main():
    arr = list(map(int, input().split()))
    if not arr:
        print()
        return
    freq = Counter(arr)
    freq_counts = Counter(freq.values())
    n = len(arr)
    output = []
    for i in range(n + 1):
        output.append(str(freq_counts.get(i, 0)))
    print(' '.join(output))

if __name__ == "__main__":
    main()