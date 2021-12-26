from heapq import heappush, heappop


def solution(jobs):
    # jobs가 정렬이 안되어있음
    jobs.sort(key=lambda x: (x[0], x[1]))

    # 0 변수 선언
    min_h = []
    jobs_idx = 0
    cur = 0
    s, rt = None, None
    running = False
    answer_list = []

    # 1 디스크 컨트롤러 with min_HEAP
    while jobs_idx < len(jobs) or min_h or running:
        if running:
            answer_list.append((rt + cur - s))
            cur += rt
            running = False
        else: # disk is not running
            while jobs_idx < len(jobs) and cur >= jobs[jobs_idx][0]:
                heappush(min_h, (jobs[jobs_idx][1], jobs[jobs_idx][0]))
                jobs_idx += 1

            if min_h:
                rt, s = heappop(min_h)
                running = True
            else:
                cur += 1
    # 2 정답 출력
    answer = sum(answer_list) // len(answer_list)
    return answer


if __name__ == '__main__':
    print(solution(	[[0, 3], [1, 9], [2, 6]]))