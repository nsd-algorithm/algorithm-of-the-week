#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> results) {
    int answer = 0;
    vector<vector <bool>> updateResults(n+1,vector<bool>(n+1,false));
    // n x n 배열을 만듬, 초기값은 false

	for (int i = 0; i <results.size(); i++){
		int winPeople = results[i][0];
		int losePeople = results[i][1];
		updateResults[winPeople][losePeople] = true;
        // 결과가 명확한 경우에만 true로 바꿈
	}
	//플로이드 와샬 알고리즘
    //a->b이고 b->c, a->c가 됨
    //거꾸로 b->a가 되는 경우 중에 a->c가 되는 경우를 찾음
    //위의 경우에만 true로 바꿈
	for (int second = 1; second <= n; second ++){
		for (int first = 1; first <= n; first ++){
			for (int third = 1; third <= n; third ++){
				if(updateResults[first][second] && updateResults[second][third]){
					updateResults[first][third] = true;
				}
			}
		}
	}

    
	//업데이트된 결과를 통해 다시 확인 함
	for (int i = 1; i<= n; i++){
		int tmp = 0;
		for (int j = 1; j <=n ; j++){
			if(i == j){
				continue;
				// 본인과 경기하는 경우는 없음  
			}
			if(updateResults[i][j] || updateResults[j][i]){
				tmp ++;
                //i번째 사람과 j번째 사람의 대결 결과가 명확하면 카운트
			}
		}
		if(tmp ==n-1){
				//자기 자신 빼고 모든 사람과 대결한 경우(승패를 확실히 알 경우)
				answer ++;
			}
	}
	
			
			 
	
    return answer;
}