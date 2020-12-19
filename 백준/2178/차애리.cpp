#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int n, m;
int dx[4] = {0, -1, 1, 0};
int dy[4] = {-1, 0, 0, 1};
int myVisit[101][101];
int myMap[101][101];
queue <pair<int, int> > q;


void bfs() {
    q.push(make_pair(0,0));
    int nx, ny;
    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();
        for (int i = 0; i < 4; i ++) {
            nx = cx + dx[i];
            ny = cy + dy[i];
            if (nx >=0 && nx < m && ny >= 0 && ny < m && myMap[nx][ny] == 1) {
                q.push(make_pair(nx,ny));
                myMap[nx][ny] = myMap[cx][cy] + 1;                
            }
        }
    }
    return ;
}



int main(void) {
    cin >> n >> m;  
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            scanf("%1d",&myMap[i][j]);
        }
    }
    bfs();
    cout << myMap[n-1][m-1];
    return 0;
}