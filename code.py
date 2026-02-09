n, d = map(int, input().split())
a = list(map(int, input().split()))

mod_counts = {0: 1}
current_sum = 0
result = 0

for num in a:
    current_sum += num
    mod = current_sum % d
    result += mod_counts.get(mod, 0)
    mod_counts[mod] = mod_counts.get(mod, 0) + 1

print(result)