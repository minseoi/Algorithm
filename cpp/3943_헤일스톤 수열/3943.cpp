//https://www.acmicpc.net/problem/3943

#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int T;
    int n;
    int maxValue;
    cin>>T;
    while(T--) {
        cin>>n;
        maxValue = n;
        while (n != 1)
        {
            if(n%2)
            {
                n = 3*n+1;
                maxValue = max(maxValue,n);
            }
            else
            {
                n/=2;
            }
        }
        printf("%d\n",maxValue);
    }
}
