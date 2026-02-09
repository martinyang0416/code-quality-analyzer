def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for _ in range(T):
        N = int(input[idx])
        idx +=1
        friends = list(map(int, input[idx:idx+N]))
        idx +=N
        total = sum(friends) - N + 1
        print(total)
        
if __name__ == "__main__":
    main()