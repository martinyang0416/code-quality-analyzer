def main():
    import sys
    input = sys.stdin.read().split()
    m = int(input[0])
    elements = list(map(int, input[1:]))
    elements.sort()

    # Check frequency condition
    freq = {}
    for num in elements:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    is_even = (m % 2 == 0)
    valid = True

    if is_even:
        for count in freq.values():
            if count % 2 != 0:
                valid = False
                break
    else: