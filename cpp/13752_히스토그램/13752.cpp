//https://www.acmicpc.net/problem/13752

#include <iostream>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, k;
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> k;
        for (int j = 0; j < k; ++j)
        {
            std::cout << '=';
        }
        std::cout << '\n';
    }
}
