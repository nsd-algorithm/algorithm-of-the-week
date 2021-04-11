#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 1;

    sort(routes.begin(), routes.end());
    int end = routes[0][1];
    for(int i = 0; i < routes.size(); i ++)
    {
      if (routes[i][0] > end)
      {
        answer ++;
        end = routes[i][1];
      }
      else if (routes[i][1] < end)
      {
        end = routes[i][1];
      }
    }
    return answer;
}