k = int(input())
if k == 0:
    print(0)
else:
    print((k - 1).bit_length())