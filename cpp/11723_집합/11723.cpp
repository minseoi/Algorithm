//https://www.acmicpc.net/problem/11723

#include <iostream>
#include <string>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int M, S = 0;
    std::string str;
    int x;
    std::cin >> M;
    for (int i = 0; i < M; ++i)
    {
        std::cin >> str;
        if (str == "add")
        {
            std::cin >> x;
            S |= (1 << x);
        }
        else if (str == "remove")
        {
            std::cin >> x;
            S &= ~(1 << x);
        }
        else if (str == "check")
        {
            std::cin >> x;
            std::cout << ((S & (1 << x)) ? 1 : 0) << '\n';
        }
        else if (str == "toggle")
        {
            std::cin >> x;
            S ^= (1 << x);
        }
        else if (str == "all")
        {
            S = (1 << 21) - 1;
        }
        else if (str == "empty")
        {
            S = 0;
        }
    }
}
