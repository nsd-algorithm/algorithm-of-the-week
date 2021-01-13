#include <iostream>
#include <algorithm>

#define MAX 200000

using namespace std;

int N,C;
int home[MAX];

bool check(int distance) {
    int router = 1;
    int pre = home[0];
    
    for(int i = 1 ; i < N; i ++) {
        if(home[i] - pre >= distance) {
            router++;
            pre = home[i];
        }
    }
    if(router >= C) {
        return true;
    }
    else {
        return false;
    }

}

int main(void) {
    cin >> N >> C;
    for (int i = 0 ; i < N; i++) {
        cin >> home[i];
    }

    sort(home, home + N);
    int left = 1;
    int right = home[N-1] - home[0];
    int answer = 0;

    // binary search part
    while(left<=right) {
        int mid = (left + right) / 2;
        if(check(mid)) {
            answer = max(answer, mid);
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    cout << answer <<endl;
    return 0;
}