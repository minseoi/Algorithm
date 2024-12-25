//https://www.acmicpc.net/problem/9655

#include <iostream>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::cout << (n%2 ? "SK" : "CY");

    return 0;
}
