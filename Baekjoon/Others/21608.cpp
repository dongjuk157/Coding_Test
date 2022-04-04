#include <iostream>
#include <vector>
using namespace std;

typedef struct Seat
{
  int num;         // student number
  int adj[4];      // u l r d
  int adj_student; // number of adjacent student
} SEAT;

SEAT arr[20][20];
int like[401][4];

void init(int size);
void renew(int size, int student, int r, int c);
int pow10(int n);
int check_empty_seat(int r, int c);
int check_satisfaction(int student, int r, int c);
int calculate_satisfaction_for_all(int size);

vector<pair<int, int>> choose_seats_first(int size, int i);
vector<pair<int, int>> choose_seats_second(vector<pair<int, int>> first_vector);

int main()
{
  // 0 initial setting
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // 1 input
  int N, i, j, k;
  cin >> N;
  init(N);
  for (i = 0; i < N * N; i++)
  {
    int student;
    cin >> student;
    cin >> like[student][0] >> like[student][1] >> like[student][2] >> like[student][3];
    // 2-1 search max adj seat vector in empty seat
    vector<pair<int, int>> tmp1 = choose_seats_first(N, student);
    if (!tmp1.size())
      continue;
    // 2-2 search adj empty seat vector in adj vector
    vector<pair<int, int>> tmp2 = choose_seats_second(tmp1);
    if (!tmp2.size())
      continue;
    // 2-3 select seat and renew information
    renew(N, student, tmp2.at(0).first, tmp2.at(0).second);
  }
  // 3 output (print)
  cout << calculate_satisfaction_for_all(N) << endl;
  return 0;
}

void init(int size)
{
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      // arr[i][j].num = 0;
      // arr[i][j].adj_student = 0;
      // arr[i][j].adj[0] = arr[i][j].adj[1] = arr[i][j].adj[2] = arr[i][j].adj[3] = 0;
      if (i == 0)
      {
        arr[i][j].adj[0] = -1; // u
      }
      else if (i == size - 1)
      {
        arr[i][j].adj[3] = -1; // d
      }

      if (j == 0)
      {
        arr[i][j].adj[1] = -1; // l
      }
      else if (j == size - 1)
      {
        arr[i][j].adj[2] = -1; // r
      }
    }
  }
}

void renew(int size, int student, int r, int c)
{
  arr[r][c].num = student;
  if (r - 1 >= 0)
  {
    arr[r - 1][c].adj[3] = student;
    arr[r - 1][c].adj_student++;
  }
  if (r + 1 < size)
  {
    arr[r + 1][c].adj[0] = student;
    arr[r + 1][c].adj_student++;
  }
  if (c - 1 >= 0)
  {
    arr[r][c - 1].adj[2] = student;
    arr[r][c - 1].adj_student++;
  }
  if (c + 1 < size)
  {
    arr[r][c + 1].adj[1] = student;
    arr[r][c + 1].adj_student++;
  }
}

int check_empty_seat(int r, int c)
{
  int ret = 0;
  for (int i = 0; i < 4; i++)
  {
    if (!arr[r][c].adj[i])
    {
      ret++;
    }
  }
  return ret;
}

int check_satisfaction(int student, int r, int c)
{
  int ret = 0;

  for (int i = 0; i < 4; i++)
  {
    if (arr[r][c].adj[i] <= 0)
      continue;
    for (int j = 0; j < 4; j++)
      if (arr[r][c].adj[i] == like[student][j])
        ret++;
  }
  return ret;
}

vector<pair<int, int>> choose_seats_first(int size, int student)
{
  vector<pair<int, int>> ret;
  int max_satisfaction = 0;
  for (int j = 0; j < size; j++)
  {
    for (int k = 0; k < size; k++)
    {
      if (arr[j][k].num)
        continue;
      int satisfaction = check_satisfaction(student, j, k);
      if (max_satisfaction < satisfaction)
      {
        max_satisfaction = satisfaction;
        ret = {};
        ret.push_back(make_pair(j, k));
      }
      else if (max_satisfaction == satisfaction)
      {
        ret.push_back(make_pair(j, k));
      }
    }
  }
  return ret;
}

vector<pair<int, int>> choose_seats_second(vector<pair<int, int>> first_vector)
{
  vector<pair<int, int>> ret;
  int max_empty_seat = 0;
  for (auto it = first_vector.begin(); it != first_vector.end(); ++it)
  {
    int empty_seat = check_empty_seat((*it).first, (*it).second);
    if (max_empty_seat < empty_seat)
    {
      max_empty_seat = empty_seat;
      ret = {};
      ret.push_back(make_pair((*it).first, (*it).second));
    }
    else if (max_empty_seat == empty_seat)
    {
      ret.push_back(make_pair((*it).first, (*it).second));
    }
  }
  return ret;
}

int pow10(int n)
{
  switch (n)
  {
  case 1:
    return 1;
  case 2:
    return 10;
  case 3:
    return 100;
  case 4:
    return 1000;
  default:
    return 0;
  }
};
int calculate_satisfaction_for_all(int size)
{

  int ret = 0;
  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < size; j++)
    {
      int student = arr[i][j].num;
      int cnt = 0;
      for (int k = 0; k < 4; k++)
      {
        for (int l = 0; l < 4; l++)
        {
          if (arr[i][j].adj[k] == like[student][l])
            cnt++;
        }
      }
      ret += pow10(cnt);
    }
  }
  return ret;
}