def solution(genres, plays):
    # 0 해시 생성
    genre_set = set()
    genre_dict = dict()
    genre_play_dict = dict()

    # 1 입력
    for i in range(len(genres)):
        if genres[i] not in genre_set:
            genre_set.add(genres[i])
            genre_dict[genres[i]] = []
            genre_play_dict[genres[i]] = 0

        genre_dict[genres[i]].append((i, plays[i]))
        genre_play_dict[genres[i]] += plays[i]

    # 2 정렬
    # 2-1 많이 재생된 장르
    max_play_order = sorted([(k, v) for k, v in genre_play_dict.items()], key=lambda x: (-x[1]))
    # 2-2 장르 내에서 많이 재생, 재생횟수가 같으면 고유번호 낮은 노래
    for lst in genre_dict.values():
        lst.sort(key=lambda x: (-x[1], x[0]))

    # 3 베스트 앨범 수록
    answer = []
    for genre, _ in max_play_order:
        MAX_LEN = 2
        genre_len = len(genre_dict[genre])
        for i in range(min(genre_len, MAX_LEN)):
            answer.append(genre_dict[genre][i][0])

    return answer