//https://www.acmicpc.net/problem/15686

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

struct Coord
{
    int r, c {};

    bool operator<(const Coord& rhs) const
    {
        if (r == rhs.r)
        {
            return c < rhs.c;
        }
        return r < rhs.r;
    }
};

struct Map
{
    std::vector<Coord> house {};
    std::vector<Coord> chicken {};
};

int CalcDist(const Coord& a, const Coord& b)
{
    return abs(a.r - b.r) + abs(a.c - b.c);
}

int CalcChickenDist(const Map& map)
{
    int chickenDist = 0;
    for (const auto& eachHouse : map.house)
    {
        int minDist = INT_MAX;
        for (const auto& eachChicken : map.chicken)
        {
            int dist = CalcDist(eachHouse, eachChicken);
            minDist = std::min(minDist, dist);
        }
        chickenDist += minDist;
    }
    return chickenDist;
}

std::vector<std::vector<Coord>> Combination(const std::vector<Coord>& vec, int r)
{
    std::vector<std::vector<Coord>> ret;
    std::vector<int> ind;
    const int n = vec.size();
    for (int i = 0; i < n - r; ++i)
    {
        ind.push_back(0);
    }
    for (int i = 0; i < r; ++i)
    {
        ind.push_back(1);
    }

    do
    {
        std::vector<Coord> array;
        for (int i = 0; i < n; ++i)
        {
            if (ind[i] == 1)
            {
                array.push_back(vec[i]);
            }
        }
        ret.push_back(array);
    } while (std::next_permutation(ind.begin(), ind.end()));
    return ret;
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Map map;
    int n, m, inputValue = 0;
    std::cin >> n >> m;
    for (int c = 0; c < n; ++c)
    {
        for (int r = 0; r < n; ++r)
        {
            std::cin >> inputValue;
            if (inputValue == 1)
            {
                map.house.push_back({c, r});
            }
            else if (inputValue == 2)
            {
                map.chicken.push_back({c, r});
            }
        }
    }

    int minChickenDist = INT_MAX;
    for (int numOfChicken = 1; numOfChicken <= m; ++numOfChicken)
    {
        std::vector<std::vector<Coord>> chickenComb = Combination(map.chicken, numOfChicken);
        for (const auto& eachComb : chickenComb)
        {
            Map tempMap = map;
            tempMap.chicken.clear();
            for (const Coord& eachCoord : eachComb)
            {
                tempMap.chicken.push_back(eachCoord);
            }
            int chickenDist = CalcChickenDist(tempMap);
            minChickenDist = std::min(minChickenDist, chickenDist);
        }
    }
    std::cout<<minChickenDist;

    return 0;
}
