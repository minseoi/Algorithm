//https://www.acmicpc.net/problem/5073

#include <iostream>

std::string GetTriangleType(int a, int b, int c)
{
    if (a + b <= c || a + c <= b || b + c <= a)
    {
        return "Invalid";
    }

    if (a == b && b == c)
    {
        return "Equilateral";
    }

    if (a == b || b == c || a == c)
    {
        return "Isosceles";
    }

    return "Scalene";
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int a, b, c;
    while (true)
    {
        std::cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0)
        {
            break;
        }
        std::cout << GetTriangleType(a, b, c) << '\n';
    }

    return 0;
}
