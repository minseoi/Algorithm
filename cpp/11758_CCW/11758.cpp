//https://www.acmicpc.net/problem/11758

#include <iostream>
#include <utility>
using namespace std;

typedef std::pair<int,int> vector2D;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    vector2D vertices[3];
    for (int i=0; i<3; i++)
    {
        cin>>vertices[i].first >> vertices[i].second;
    }
    
    int crossResult = (vertices[1].first - vertices[0].first) * (vertices[2].second - vertices[0].second) - (vertices[1].second - vertices[0].second) * (vertices[2].first - vertices[0].first);
    if(crossResult == 0)
        cout<<0;
    else if(crossResult > 0)
        cout<<1;
    else if(crossResult < 0)
        cout<<-1;
}
