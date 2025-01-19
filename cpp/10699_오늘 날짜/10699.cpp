//https://www.acmicpc.net/problem/10699

#include <iostream>
#include <chrono>
#include <ctime>
#include <iomanip>

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
    std::tm utcNow = *std::gmtime(&now);

    std::cout << std::put_time(&utcNow, "%Y-%m-%d");
    return 0;
}
