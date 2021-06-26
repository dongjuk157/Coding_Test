def solution(m, musicinfos):
    answer = ''
    answer_playtime = 0
    for info in musicinfos:
        # 문자열 파싱
        s, e, title, melody = info.split(',')
        sh, sm = map(int, s.split(':'))
        sm_total = sh * 60 + sm
        eh, em = map(int, e.split(':'))
        em_total = eh * 60 + em
        playtime = em_total - sm_total

        # "x"인지 "x#"인지 확인하기 위해 m의 각 음계마다 분리(쉼표를 넣어줌)
        tmp_m = []
        for i in range(len(m)):
            if m[i] == "#":
                continue
            elif i + 1 < len(m) and m[i + 1] == "#":
                tmp_m.append(m[i:i + 2])
            else:
                tmp_m.append(m[i])
        tmp_m2 = ''
        for i in range(len(tmp_m)):
            tmp_m2 += tmp_m[i] + ','

        #  melody의 각 음계마다 분리(쉼표를 넣어줌)
        tmp_melody = []
        for i in range(len(melody)):
            if melody[i] == "#":
                continue
            elif i + 1 < len(melody) and melody[i + 1] == "#":
                tmp_melody.append(melody[i:i + 2])
            else:
                tmp_melody.append(melody[i])
        # playtime만큼 멜로디 작성
        tmp_melody2 = ''
        for i in range(playtime):
            tmp_melody2 += tmp_melody[i % len(tmp_melody)] + ','

        # 쉼표를 포함한 멜로디가 포함되어있을때, 플레이타임이 가장 긴 제목 저장
        if tmp_m2 in tmp_melody2:
            if answer_playtime < playtime:
                answer = title
                answer_playtime = playtime

    return answer if answer else "(None)"