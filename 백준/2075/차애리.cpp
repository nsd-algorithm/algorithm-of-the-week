#include <iostream>
#include <queue>
#include <vector>

using namespace std;

 
int main(void)
{
    int n, now;
	
	
	cin >> n;
	
	vector <vector<int>> v (n, vector<int>(n));
	for (int i = 0; i < n; i ++)
	{
		for (int j = 0; j < n; j ++)
		{
			cin >> v[i][j];
		}
	}
    priority_queue <int, vector<int>, greater<int> > pq;
	
	for (int i = 0; i < n; i++)
	{
		pq.push(v[n-1][i]);
	}
	
	for (int i = 0; i < v.size(); i++)
	{
		for (int j = 0; j < n; j ++)
		{
			cout << v[i][j] << "  ";
		}
		cout << "\n";
	}
	
    return 0;
}