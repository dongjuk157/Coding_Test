def solution(msg):
    answer = []
    # 1 사전 초기화
    dic = dict(zip(map(chr, range(ord('A'), ord('Z') + 1)), range(1, 27)))

    msg_index, dic_index = 0, 27
    while msg_index < len(msg):
        # 2 가장 긴 문자열 검색
        tmp_ind = 1
        while msg_index + tmp_ind <= len(msg) and dic.get(msg[msg_index:msg_index + tmp_ind]):
            tmp_ind += 1

        # 3 w에 해당하는 사전의 색인 번호를 출력
        answer.append(dic[msg[msg_index:msg_index + tmp_ind - 1]])

        # 4 다음글자 남아있으면 단어를 사전에 등록
        if not dic.get(msg[msg_index:msg_index + tmp_ind]):
            dic[msg[msg_index:msg_index + tmp_ind]] = dic_index
            dic_index += 1

        # 5 2반복
        msg_index += tmp_ind - 1

    return answer

if __name__ == "__main__":
    msg = ["KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"]
    answer = [
        [11, 1, 27, 15],
        [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
        [1, 2, 27, 29, 28, 31, 30]
    ]

    for i in range(len(msg)):
        my_answer = solution(msg[i])
        print(my_answer == answer[i])
