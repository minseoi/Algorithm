//https://www.acmicpc.net/problem/2914

#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int A, I;
    cin>>A>>I;
    printf("%d", A*(I-1)+1);
}
