# from sys import stdin; input = stdin.readline
from itertools import permutations

def main():
    # 0 input
    N = int(input())
    innings = [list(map(int, input().split())) for _ in range(N)]

    # 1 bruteforce
    max_score = 0
    # 1-1 make permutation
    for player_order_first in permutations(range(2, 10), 3):
        # 1-2 calculate max value / simulation
        other_players = set(range(2, 10)) - set(player_order_first)
        for player_order_second in permutations(other_players, 5):
            player_order = [*player_order_first, 1, *player_order_second]
            player_idx = 0
            score = 0
            for inning in innings:
                out = 0
                bases = [0 for _ in range(3)] # 1st ~ 3rd base
                while out < 3:
                    cur_player = player_order[player_idx] - 1
                    if 0 == inning[cur_player]:
                        out += 1
                    elif 1 == inning[cur_player]:
                        score += bases[2]
                        bases[0], bases[1], bases[2] = 1, bases[0], bases[1]
                    elif 2 == inning[cur_player]:
                        score += bases[1] + bases[2]
                        bases[0], bases[1], bases[2] = 0, 1, bases[0]
                    elif 3 == inning[cur_player]:
                        score += sum(bases)
                        bases[0], bases[1], bases[2] = 0, 0, 1
                    elif 4 == inning[cur_player]:
                        score += sum(bases) + 1
                        bases[0], bases[1], bases[2] = 0, 0, 0
                    player_idx = (player_idx + 1) % 9

            max_score = max(max_score, score)

    # 2 output
    print(max_score)

if __name__ == "__main__":
    main()
