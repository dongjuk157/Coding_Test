while True:
    s_list = input().split()
    ch = s_list[0]
    if ch == '#':
        break
    s = ''.join(s_list[1:])
    result = 0
    for ch_s in s:
        if ch == ch_s.lower():
            result += 1
    print(ch, result)