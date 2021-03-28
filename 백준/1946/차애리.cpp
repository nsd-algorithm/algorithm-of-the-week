#include <bits/stdc++.h>

using namespace std;

bool compare(const pair<int,int>&a, const pair<int,int>&b){
    return a.first<b.first;
}

int solution(int len, vector <pair<int,int>> people){

    sort(people.begin(),people.end(),compare);

    int cnt = 1;
    int minn = people[0].second;
    for(int i = 0; i < len; i++){
        if(people[i].second <minn){
            cnt++;
            minn = people[i].second;
        }
    }
    return cnt;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >>n;
    for (int i = 0; i < n; i++){
        vector <pair<int,int>> v;
        int l;
        cin >>l;
        for(int j = 0;j<l; j++){
            int x,y;
            cin >>x>>y;
            v.push_back(make_pair(x,y));
        }
        cout <<solution(v.size(),v) << '\n';
    }
}