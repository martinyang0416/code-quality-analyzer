m = int(input())
solutions = set()

for s in range(1, 82):  # since sum of digits can't exceed 81
    if m % s == 0:
        y = m // s
        sum_digits = sum(int(d) for d in str(y))
        if sum_digits == s:
            solutions.add(y)

sorted_solutions = sorted(solutions)
print(len(sorted_solutions))
for y in sorted_solutions:
    print(y)