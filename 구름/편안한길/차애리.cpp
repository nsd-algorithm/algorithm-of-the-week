#include <iostream>
#include <vector>
#include <queue>
using namespace std;



// recursion으로 푼게 아님 다시 풀어야 함
int myMap[101][101];
int visit[101][101];
int dx[4] = {-1,0,0,1};
int dy[4] = {-1,0,1,0};

int main() {
	int input;
	cin >> input;
	//vector <vector<int>> v(input, vector<int>(input,0));
	//vector<vector <int>> v;
	
	
	queue <pair <int, int>> q;
	for(int i = 0; i < input ; i++){
		for(int j = 0; j < input; j++){
			cin >> myMap[i][j];
		}
	}
	
	q.push(make_pair(0,0));
	while(!q.empty()){
		pair <int, int> current_position = q.front();
		int x = current_position.first;
		int y = current_position.second;
		q.pop();
		for(int dir = 2; dir < 4; dir++){
			int cx = x + dx[dir];
			int cy = y + dy[dir];
			if(cx<0 || cy <0 || cx > input || cy > input){
				continue;
			}
			if(visit[cx][cy] == 0){
				visit[cx][cy] = visit[x][y] + myMap[cx][cy];
				//cout << "myMap[cx][cy] : " << myMap[cx][cy] <<'\n';
				q.push(make_pair(cx,cy));
			}
			else if(visit[cx][cy] < visit[x][y] + myMap[cx][cy]) {
				visit[cx][cy] = visit[x][y] + myMap[cx][cy];
				q.push(make_pair(cx,cy));
			}
		}
	}
		
	for(int i = 0; i < input ; i++){
		for(int j = 0; j < input; j++){
			cout << visit[i][j] << ' ';
		}
		cout << '\n';
	}
	
	cout << "Hello Goorm! Your input is " << visit[input-1][input-1] << endl;
	return 0;
}