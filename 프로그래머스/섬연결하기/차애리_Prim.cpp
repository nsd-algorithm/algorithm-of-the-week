#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <iostream>

#define MAX 101
using namespace std;


int visited[MAX]; // 방문 여부를 담을 배열
vector<pair<int, int>> v[MAX];

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;

    // costs 배열에서 각 섬의 정보를 v 정점 배열에 다시 저장
    for (int i = 0; i < costs.size(); i++) {
        int n1 = costs[i][0];
        int n2 = costs[i][1];
        int cost = costs[i][2];

        // 시작정점.(끝정점, 비용)
        v[n1].push_back(make_pair(n2, cost));
        v[n2].push_back(make_pair(n1, cost));
    }

    // greater를 쓰면 오름차순 우선순위 큐를 만들 수 있음
    // priority_queue <pair<int, int>> pq;
    priority_queue <pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (int i = 0; i < v[0].size(); i ++) {
        cout << i << endl;
        int next_n = v[0][i].first;
        int next_cost = v[0][i].second;
        pq.push(make_pair(next_cost, next_n));
    }

    // 0번째 섬 방문 체크
    visited[0] = 1;

    while(!pq.empty()) {
        int expect_cost = pq.top().first;
        int current_n = pq.top().second;
        pq.pop();

        if(visited[current_n] == 0) {
            visited[current_n] = 1;
            answer += expect_cost;
            // 아래 부분이 이해 안감...
            for (int i = 0; i < v[current_n].size(); i ++) {
                cout << i << endl;
                int next_n = v[current_n][i].first;
                int next_cost = v[current_n][i].second;
                if(visited[next_n] == 0) {
                    pq.push(make_pair(next_cost, next_n));
                }
                
            }
        }
    }
    return answer;
}

