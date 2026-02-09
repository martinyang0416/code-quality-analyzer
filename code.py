from collections import Counter

def main():
    W = input().strip()
    m = int(input().strip())
    cards = input().split()
    
    word_counts = Counter(W)
    card_counts = Counter(cards)
    
    possible = True
    for char, count in word_counts.items():
        if card_counts[char] < count:
            possible = False
            break
    
    print("YES" if possible else "NO")

if __name__ == "__main__":
    main()