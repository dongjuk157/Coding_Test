import sys; input = sys.stdin.readline

def stringToMinutes(string):
    hh, mm = map(int, string.split(":"))
    return hh * 60 + mm

def main():
    S, E, Q = map(stringToMinutes, input().split())
    answer = 0
    attendance = dict()
    attendance_after = dict()
    # while True:
    try:
        while 1:
            line = input()
            st, nickname = line.split()
            mm = stringToMinutes(st)
            if mm <= S:
                if not attendance.get(nickname):
                    attendance[nickname] = True
            elif E <= mm <= Q:
                if attendance.get(nickname) and not attendance_after.get(nickname):
                    attendance_after[nickname] = True
                    answer += 1
    except:
        print(answer)

if __name__ == '__main__':
    main()

