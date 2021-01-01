//1. 인원 수 보다 작은 돌을 찾음(이분탐색-left)
//2. 만약 인원 수보다 작은 돌이 k-1번이하 있으면 통과, k초과면 false 
 

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// true면 인원수 증가 시킴
// false면 break
bool check(vector<int> stones, int k, int mid) {
    int tmp = 0;
    for (int i = 0; i < stones.size(); i ++) {
        if(stones[i] < mid) {
            tmp ++;
            if(tmp >= k) {
                return false;
            }
        }
        else {
            tmp = 0;
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;

    int r_value = * max_element(stones.begin(), stones.end());
    int l_value = 1;

    while(l_value<=r_value) {
        int mid = (l_value + r_value) / 2;
        if(check(stones, k, mid)) {
            l_value = mid + 1;
            if(answer < mid) {
                answer = mid;
            }
        }
        else {
            r_value = mid - 1;
        }
    }

    return answer;
}