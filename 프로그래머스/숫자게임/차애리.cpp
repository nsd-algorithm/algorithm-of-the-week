#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    int idxA = 0;
    int idxB = 0;
    while(1){
    	if(A[idxA]<B[idxB]){
    		idxA+=1;
    		idxB+=1;
    		answer+=1;
    	}
    	else{
    		idxB+=1;
    	}
    	if(idxA == A.size() || idxB == B.size()){
    		break;
    	}
    }
    return answer;
}
