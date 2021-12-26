from heapq import heappush, heappop

def solution(operations):
    answer = [0, 0]
    min_h, max_h = [], []
    number_in_heap = dict()
    for op in operations:
        if op[0] == 'I': # 숫자 삽입
            _, num = op.split()
            num = int(num)
            heappush(min_h, num)
            heappush(max_h, -num)
            if not number_in_heap.get(num):
                number_in_heap[num] = 0
            number_in_heap[num] += 1
        else:
            if op[2] == '1': # 최댓값 삭제
                while max_h:
                    tmp_number = -heappop(max_h)
                    if number_in_heap[tmp_number]:
                        number_in_heap[tmp_number] -= 1
                        break
            else: # 최솟값 삭제
                while min_h:
                    tmp_number = heappop(min_h)
                    if number_in_heap[tmp_number]:
                        number_in_heap[tmp_number] -= 1
                        break

    while min_h:
        tmp_number = heappop(min_h)
        if number_in_heap[tmp_number]:
            answer[1] = tmp_number
            break
    while max_h:
        tmp_number = -heappop(max_h)
        if number_in_heap[tmp_number]:
            answer[0] = tmp_number
            break

    return answer

if "__main__" == __name__:
    print(solution(["I 7","I 5","I -5","D -1"]))
    print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))