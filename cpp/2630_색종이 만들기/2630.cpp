//https://www.acmicpc.net/problem/2630

#include <iostream>

#define COLOR_BLUE 1
#define COLOR_WHITE 0

int paper[128][128] {};
int numOfBlue = 0;
int numOfWhite = 0;

void CountPieces(int startH, int startW, int size)
{
    bool bShouldCut = false;
    const int reference = paper[startH][startW];
    for (int h = 0; h < size; ++h)
    {
        for (int w = 0; w < size; ++w)
        {
            if (paper[startH + h][startW + w] != reference)
            {
                bShouldCut = true;
                break;
            }
        }
        if (bShouldCut)
        {
            break;
        }
    }

    if (bShouldCut)
    {
        const int halfSize = size * 0.5f;
        CountPieces(startH, startW, halfSize);
        CountPieces(startH + halfSize, startW, halfSize);
        CountPieces(startH, startW + halfSize, halfSize);
        CountPieces(startH + halfSize, startW + halfSize, halfSize);
    }
    else
    {
        if (reference == COLOR_BLUE)
        {
            ++numOfBlue;
        }
        else if (reference == COLOR_WHITE)
        {
            ++numOfWhite;
        }
    }
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, inputValue;
    std::cin >> n;
    for (int h = 0; h < n; ++h)
    {
        for (int w = 0; w < n; ++w)
        {
            std::cin >> paper[h][w];
        }
    }

    CountPieces(0, 0, n);
    std::cout << numOfWhite << '\n' << numOfBlue;
}
