//https://www.acmicpc.net/problem/23971

#include <iostream>
#include <cmath>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int w, h, n, m;
    std::cin >> w >> h >> n >> m;

    int space_w = static_cast<int>(std::ceil(static_cast<float>(w) / (n + 1)));
    int space_h = static_cast<int>(std::ceil(static_cast<float>(h) / (m + 1)));

    std::cout << space_w * space_h;

    return 0;
}
