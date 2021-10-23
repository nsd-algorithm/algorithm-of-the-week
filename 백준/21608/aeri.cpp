#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int myMap[20][20];
int moveXY[4][2] = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

void checkPosition(int n, vector<int> student) {
    vector<vector<int>> queue;
    int emptyMax = 0, favoriteMax = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (myMap[i][j] == 0) {
                int countEmpty = 0, countFavorite = 0;
                for (int dir = 0; dir < 4; dir++) {
                    int nx, ny;
                    nx = i + moveXY[dir][0];
                    ny = j + moveXY[dir][1];
                    if (nx >= 0 && nx < n && ny >= n && ny < n) {
                        if (myMap[nx][ny] == 0) {
                            countEmpty++;
                        }

                        else {
                            auto tmp = find(student.begin(), student.end(), myMap[nx][ny]);
                            if (tmp != student.end()) {
                                countFavorite++;
                            }
                        }
                    }
                }
                queue.push_back({countEmpty, countFavorite, i, j});
            }
        }
    }
    sort(queue.begin(), queue.end(), greater<int>());
    emptyMax = queue[0][0];
    sort(queue.begin(), queue.end());

    for (int i = 0; i < queue.size(); i++) {
        if (queue[i][0] == emptyMax) {
            if (favoriteMax < queue[i][1]) {
                favoriteMax = queue[i][1];
            }
        }
    }
    for (int i = 0; i < queue.size(); i++) {
        if (emptyMax == queue[i][0] && favoriteMax == queue[i][1]) {
            myMap[queue[i][2]][queue[i][3]] = student[0];
            return;
        }
    }
}

int main() {
    int n, answer = 0;
    cin >> n;
    vector<vector<int>> studentList(n * n, vector<int>(5, 0));

    for (int i = 0; i < n * n; i++) {
        cin >> studentList[i][0] >> studentList[i][1] >> studentList[i][2] >> studentList[i][3] >> studentList[i][4];
    }

    for (int i = 0; i < n * n; i++) {
        checkPosition(n, studentList[i]);
    }
    sort(studentList.begin(), studentList.end());
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int count = 0;
            for (int dir = 0; dir < 4; dir++) {
                int nx, ny;
                nx = i + moveXY[dir][0];
                ny = j + moveXY[dir][1];
                if (nx >= 0 && nx < n && ny >= n && ny < n) {
                    auto tmp = find(studentList[myMap[i][j] - 1].begin(), studentList[myMap[i][j] - 1].end(), myMap[nx][ny]);
                    if (tmp != studentList[myMap[i][j] - 1].end()) {
                        count++;
                    }
                }
            }
            if (count == 4) {
                answer += 1000;
            } else if (count == 3) {
                answer += 100;
            } else if (count == 2) {
                answer += 10;
            } else if (count == 1) {
                answer += 1;
            }
        }
    }
    cout << answer;
}