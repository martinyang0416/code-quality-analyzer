s = input().strip()
if not s:
    print(s)
else:
    s_list = list(s)
    for i in range(1, len(s_list)):
        c = s_list[i]
        if c == 'z':
            s_list[i] = 'a'
        else:
            s_list[i] = chr(ord(c) + 1)
    print(''.join(s_list))