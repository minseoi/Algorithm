//https://www.acmicpc.net/problem/14182

#include <iostream>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    while (true)
    {
        std::cin >> n;
        if (n == 0)
        {
            break;
        }

        if (n > 5000000)
        {
            n *= 0.8f;
        }
        else if (n > 1000000)
        {
            n *= 0.9f;
        }
        std::cout << n << '\n';
    }
}
