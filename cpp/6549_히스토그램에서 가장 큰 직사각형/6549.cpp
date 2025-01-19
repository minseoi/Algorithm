//https://www.acmicpc.net/problem/6549

#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <utility>

using INDEX = int;
using HEIGHT = int;

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string inputLine {};
    std::vector<HEIGHT> histogram;
    INDEX n;
    while (std::getline(std::cin, inputLine))
    {
        std::stringstream ss(inputLine);
        histogram.clear();
        HEIGHT input;
        std::stack<std::pair<INDEX, HEIGHT>> stack;
        if (ss >> input)
        {
            if (input == 0)
            {
                break;
            }

            while (ss >> input)
            {
                histogram.emplace_back(input);
            }
        }

        histogram.emplace_back(0);
        unsigned long long maxArea = 0;
        const INDEX histogramSize = histogram.size();
        for (INDEX i = 0; i < histogramSize; ++i)
        {
            INDEX targetIndex = i;
            const HEIGHT targetHeight = histogram[i];
            while (!stack.empty())
            {
                const std::pair<INDEX, HEIGHT>& top = stack.top();
                if (top.second > targetHeight)
                {
                    stack.pop();
                    maxArea = std::max(maxArea, 1ULL * (i - top.first) * top.second);
                    targetIndex = top.first;
                }
                else
                {
                    break;
                }
            }
            stack.emplace(targetIndex, targetHeight);
        }
        std::cout << maxArea << '\n';
    }
}
