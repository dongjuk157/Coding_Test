#include <iostream>
#include <array>
#include <vector>
#include <algorithm> // next_permutation
using namespace std;
#define NUM_PLAYERS 9

bool play(int cur_player_play, int &score, array<int, 3> &bases)
{
  // cout << cur_player_play << " bases: ";
  // for (int i = 0; i < 3; i++)
  // {
  //   cout << bases[i] << " ";
  // }
  // cout << endl;

  // cout << "before score: " << score << endl;
  switch (cur_player_play)
  {
  case 0:
    return true;
  case 1:
    score += bases[2];
    bases[2] = bases[1];
    bases[1] = bases[0];
    bases[0] = 1;
    break;
  case 2:
    score += bases[1] + bases[2];
    bases[2] = bases[0];
    bases[1] = 1;
    bases[0] = 0;
    break;
  case 3:
    score += bases[0] + bases[1] + bases[2];
    bases[2] = 1;
    bases[1] = 0;
    bases[0] = 0;
    break;
  case 4:
    score += bases[0] + bases[1] + bases[2] + 1;
    bases[2] = 0;
    bases[1] = 0;
    bases[0] = 0;
    break;
  default:
    break;
  }

  // cout << "after score: " << score << endl;
  return false;
}

int main()
{
  // 0 initial setting
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // 1 input
  int N;
  cin >> N;
  vector<array<int, 9>> innings;
  for (int i = 0; i < N; i++)
  {
    array<int, 9> inning;
    for (int j = 0; j < 9; j++)
    {
      cin >> inning[j];
    }
    innings.push_back(inning);
  }
  // 2 bruteforce
  int max_score = 0;
  // 2-1 make permutations
  array<int, 9> players_order = {1, 2, 3, 4, 5, 6, 7, 8, 9};
  int break_cnt = 0;
  do
  {
    if (players_order[3] != 1)
      continue;

    int player_idx = 0;
    int score = 0;
    for (int i = 0; i < N; ++i) // inning start, inning = innings[i]
    {
      int out = 0;
      array<int, 3> bases = {0, 0, 0};
      while (out < 3)
      {
        int cur_player = players_order[player_idx] - 1;
        if (play(innings[i][cur_player], score, bases))
        {
          out++;
        }
        player_idx = (player_idx + 1) % 9;
      }
    }
    if (max_score < score)
    {
      max_score = score;
    }

  } while (next_permutation(players_order.begin(), players_order.end()));

  // 3 output
  cout << max_score << '\n';

  return 0;
}