//https://www.acmicpc.net/problem/2166

#include <iostream>
#include <utility>
using namespace std;

typedef std::pair<double,double> vector2D;

double GetTriangleArea(vector2D a, vector2D b, vector2D c)
{
    /* Convert to Relative Begin */
    b.first -= a.first;
    b.second -= a.second;
    c.first -= a.first;
    c.second -=a.second;
    /* Convert to Relative End */

    return (b.first*c.second - b.second*c.first) * 0.5f;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int N;
    cin >> N;
    
    vector2D* vertices = new vector2D[N];
    for (int i=0; i<N; i++)
    {
        cin>>vertices[i].first >> vertices[i].second;
    }
    
    double result = 0;
    for (int i=1; i<N-1; i++)
    {
        result += GetTriangleArea(vertices[0], vertices[i], vertices[i+1]);
    }
    result = result<0? result*-1:result;
    
    cout.precision(1);
    cout << fixed << result;
    
    free(vertices);
    vertices = nullptr;
}
