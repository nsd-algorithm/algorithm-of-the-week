#include <vector>
#include <string>
#include <algorithm>

#define MAX 101
using namespace std;


int parent[MAX]; // 각 index 별 부모 노드 정보를 담을 배열
vector <pair <int, pair<int, int>>> Edge;

//루트 노드가 아니면 루트 노드를 찾을 때까지 재귀적으로 호출함
int find_parent(int index) {
    if(index == parent[index]) {
        return index;
    }
    else {
        return parent[index] = find_parent(parent[index]);
    }
}

// 두 노드를 합치기
void union_node(int a, int b) {
    a = find_parent(a);
    b = find_parent(b);
    parent[b] = a;
}

bool same_parent(int a, int b) {
    a = find_parent(a);
    b = find_parent(b);
    if(a == b) {
        return true;
    }
    else {
        return false;
    }
}


int solution(int n, vector<vector<int>> costs) {
    int answer = 0;

    // 1. 처음 부모 노드는 각자 자신 노드로 설정
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }
    for (int i = 0; i < costs.size(); i++) {
        int node1 = costs[i][0];
        int node2 = costs[i][1];
        int cost = costs[i][2];
        Edge.push_back(make_pair(cost, make_pair(node1, node2)));
    }
    // 2. 오름차순 정렬

    sort(Edge.begin(), Edge.end());
    
    for (int i = 0; i < Edge.size(); i ++) {

        // 3. 부모노드가 같지 않으면
        if(same_parent(Edge[i].second.first, Edge[i].second.second) == false) {
            // 4. Union -> 연결하고 부모노드 정보 업데이트
            union_node(Edge[i].second.first, Edge[i].second.second);
            // 5. cost 더함
            answer += Edge[i].first;
        }
    }
    return answer;
}