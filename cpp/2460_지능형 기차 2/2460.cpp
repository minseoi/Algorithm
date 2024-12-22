//https://www.acmicpc.net/problem/2460

#include <iostream>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int totalCount = 0;
    int biggestCount = 0;
    int inCount = 0;
    int outCount = 0;
    for (int i = 0; i < 10; ++i)
    {
        std::cin >> outCount >> inCount;
        totalCount += inCount - outCount;
        biggestCount = totalCount > biggestCount ? totalCount : biggestCount;
    }
    std::cout << biggestCount << std::endl;
    return 0;
}
