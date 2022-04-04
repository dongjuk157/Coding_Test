#include <iostream>
using namespace std;
int main()
{
  // 0 initial setting
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // 1 input
  int N;
  cin >> N;
  int arr[1005] = {
      0,
  };

  for (int i = 0; i <= N; i++)
  {
    if (!arr[i])
    {
      arr[i + 3] = !arr[i];
      arr[i + 1] = !arr[i];
    }
  }

  if (arr[N])
    cout << "SK" << endl;
  else
    cout << "CY" << endl;
  return 0;
}