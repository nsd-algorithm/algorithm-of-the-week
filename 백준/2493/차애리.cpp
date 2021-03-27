#include <iostream>
#include <algorithm>
#include <stack>





using namespace std;


int myMap[500001];

int main(){
    int input,currentNum,maxNum;
    cin >> input;
    cin >> currentNum;
    maxNum = currentNum;
    for (int i = 1 ; i < input ; i ++){
        cin >> currentNum;
        if (maxNum < currentNum) {
            maxNum = currentNum;
            
        }

    }

}