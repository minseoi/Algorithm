//https://www.acmicpc.net/problem/11382

#include <iostream>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    unsigned long long input, result {};
    for (int i = 0; i < 3; ++i)
    {
        std::cin >> input;
        result += input;
    }
    std::cout << result;
    return 0;
}
