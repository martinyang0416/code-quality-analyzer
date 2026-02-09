n = int(input())
digits = input().split()

result = []
for i in range(n):
    d = digits[i]
    if (i + 1) % 2 == 1:  # Odd index operation
        result.append(d)
    else:  # Even index operation
        if not result:
            result.append(d)
        else:
            last = result[-1]
            if d == last:
                result.append(d)
            else:
                # Remove all trailing same as last
                while result and result[-1] == last:
                    resu