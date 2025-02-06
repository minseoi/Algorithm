//https://www.acmicpc.net/problem/11659

#include <iostream>
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, i, j, sum = 0;
    int array[100001];
    int sumArray[100001];
    cin>>N>>M;
    for (int n=1;n<=N;++n)
    {
        cin>>array[n];
        sum += array[n];
        sumArray[n] = sum;
    }
    for (int m=0;m<M;++m)
    {
        cin>>i>>j;
        if (i-1 > 0)
        {
            cout<<sumArray[j] - sumArray[i-1]<<'\n';
        }
        else
        {
            cout<<sumArray[j]<<'\n';
        }
    }
}