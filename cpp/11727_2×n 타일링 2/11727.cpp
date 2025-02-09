https://www.acmicpc.net/problem/11727

#include <iostream>
using namespace std;

int cache[1001] {};

int CalcCase(int n)
{
    int ret;
    if (n == 1)
    {
        ret = 1;
    }
    else if ( n==2 )
    {
        ret = 3;
    }
    else
    {
        if (cache[n] != 0)
        {
            ret = cache[n];
        }
        else
        {
            ret = (CalcCase(n-2) * 2) + (CalcCase(n-1));
            cache[n] = ret;
        }
    }
    return ret % 10007;
}

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    cin>>n;
    cout << CalcCase(n);
}