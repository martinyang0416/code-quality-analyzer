import itertools

def main():
    n = int(input())
    phrases = [input().strip() for _ in range(n)]
    
    vowels = 'aeiou'
    max_length = 0
    
    # Generate all possible subsets of 1 or 2 vowels
    for r in range(1, 3):
        for subset in itertools.combinations(vowels, r):
            allowed = set(subset)
            total = 0
            for phrase in phrases:
                phrase_vowels = set()
                for c in phrase:
                    if c in vowels:
               