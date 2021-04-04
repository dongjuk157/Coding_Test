def solution(s):
    len_s = len(s)
    answer = len_s
    if len_s == 1:
        return answer
    cnt = 1
    while cnt < len_s //2 + 1:
        i = 0
        zip_val = 0
        zip_string = ''
        while i < len_s:
            tmp_s = s[i:i + cnt]
            if tmp_s == s[i + cnt:i + 2 * cnt]:
                zip_val += 1
            else:
                if zip_val:
                    zip_string += str(zip_val+1) + tmp_s
                else:
                    zip_string += tmp_s
                zip_val = 0
            i += cnt
        else:
            zip_string += s[i+cnt:]
        cnt += 1
        if len(zip_string) < answer:
            answer = len(zip_string)
    return answer