//https://www.acmicpc.net/problem/2751

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> vec;
int main()
{
    int N;
    int num;
    cin>>N;
    for (int i=0; i<N; i++)
    {
        cin>>num;
        vec.push_back(num);
    }
    
    sort(vec.begin(), vec.end());
    
    for (int i=0; i<N; i++)
    {
        cout<<vec[i]<<'\n';
    }
    
    return 0;
}
