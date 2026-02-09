import bisect

n = int(input())
arr = list(map(int, input().split()))

tails = []
prev_map = {}

for num in arr:
    j = bisect.bisect_left(tails, num)
    if j == 0:
        prev = None
    else:
        prev = tails[j-1]
    prev_map[num] = prev
    if j == len(tails):
        tails.append(num)
    else:
        tails[j] = num

# Reconstruct the LIS
sequence = []
current = tails[-1]
while current is not None:
    sequence.append(current)
    current = prev_map[current]

sequence.reverse()

pri