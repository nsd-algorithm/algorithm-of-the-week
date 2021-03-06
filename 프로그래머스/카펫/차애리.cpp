#include <algorithm>
#include <vector>
#include <string>

using namespace std;


//전체 카페트는 적어도 길이가 3이상이어야 한다
//brown + yellow 는 전체 카페트 넓이이다
// h(세로)가 3이상부터 탐색을 하자
// yellow 카펫 수는 다음과 같이 구할 수 있다
// 최소 임의의 높이를 전체 카펫 수로 나눈다 = 전체 가로
//전체 가로 x 전체 세로 = brown+yellow이다
// (전체 가로 -2) x (전체 세로  -2) = yellow 가로 x yellow 세로 =  yellow 카펫 갯수 
//위의 조건이 맞는 yellow 가로 세로를 찾으면 됨
 

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    
    int totalnum = brown + yellow;
    int total_h = 3;
    int total_w;
    //3부터 시작
    for(int i = 3; ; i++){
    	if(totalnum%i == 0){
    		total_w =  totalnum/i;
    		if((total_w - 2) * (i -2) == yellow){
    			total_h = i;
				break;
			}
		}
	}
	answer.push_back(total_w);
	answer.push_back(total_h);
    return answer;
}