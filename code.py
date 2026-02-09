m = int(input())
A = list(map(int, input().split()))
n = int(input())
B = list(map(int, input().split()))
C = A + B
max_val = max(C)
min_val = min(C)
result = max_val - min_val
print("{0:.9f}".format(result))