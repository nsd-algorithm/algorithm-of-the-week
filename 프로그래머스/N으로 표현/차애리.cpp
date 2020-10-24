#include <iostream>
#include <unordered_set>
#include <vector>
#include <cmath>
#include <string>

using namespace std;


int solution(int N, int number){
    int answer = -1;
    int MIN = 8;
    int base = 0;
    unordered_set<int> numbers[MIN];
    for(int i = 0; i < MIN; i++){
        base = 10 * base + 1;
        numbers[i].insert(base*N);
    }

    for(int i = 0; i< MIN; i++){
        for(int j = 0; j <i ; j++){
            for (auto op1 : numbers[j]){
                for(auto op2 : numbers[i-j-1]){
                    numbers[i].insert(op1+op2);
                    numbers[i].insert(op1-op2);
                    numbers[i].insert(op1*op2);
                    if(op2!=0){
                        numbers[i].insert(op1/op2);
                    }

                }
            }
        }
        if(numbers[i].count(number) >0){
            answer = i + 1;
            break;
        }
    }
    return answer;

}
