//https://www.acmicpc.net/problem/2592

#include <iostream>
#include <unordered_map>

constexpr int ITERATIONS = 10;
using Key = int;
using Count = int;

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::unordered_map<Key, Count> counts;
    Key average = 0;
    for (int i = 0; i < ITERATIONS; ++i) {
        Key key;
        std::cin >> key;
        average += key;
        ++counts[key];
    }

    Key mode = 0;
    Count max_count = 0;
    for (const auto& [key, count] : counts)
    {
        if (count > max_count) {
            mode = key;
            max_count = count;
        }
    }
    std::cout << average / ITERATIONS << '\n';
    std::cout << mode << '\n';
    return 0;
}
