//https://www.acmicpc.net/problem/1027

#include <iostream>

#define BUILDING_MAX 50

int buildings[BUILDING_MAX] {};

int CountVisibleBuildings(int size, int baseIndex, int startIndex, int endIndex, int step)
{
    const auto CanLoop = [](const int i, const int endIndex, const int step)
    {
        if (step < 0)
        {
            return i >= endIndex;
        }
        else
        {
            return i <= endIndex;
        }
    };

    int numOfBuildings = 0;
    double prevGradient = 0;
    for (int i = startIndex; CanLoop(i, endIndex, step); i += step)
    {
        const double gradient = static_cast<double>(buildings[i] - buildings[baseIndex]) / std::abs(baseIndex - i);
        if (i != startIndex && gradient <= prevGradient)
        {
            continue;
        }

        prevGradient = gradient;
        ++numOfBuildings;
    }
    return numOfBuildings;
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, h;
    std::cin >> n;
    for (int i = 0; i < n; i++)
    {
        std::cin >> h;
        buildings[i] = h;
    }

    int result = 0;
    for (int i = 0; i < n ; ++i)
    {
        int numOfBuildings = 0;
        numOfBuildings += CountVisibleBuildings(n, i, i - 1, 0, -1) + CountVisibleBuildings(n, i, i + 1, n - 1, 1);
        result = std::max(numOfBuildings, result);
    }
    std::cout << result;
}
