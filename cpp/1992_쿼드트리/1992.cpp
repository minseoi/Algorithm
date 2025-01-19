//https://www.acmicpc.net/problem/1992

#include <iostream>
#include <string>

int image[64][64] {};

void MakeQuadTree(int startH, int startW, int size)
{
    bool bShouldCut = false;
    const int reference = image[startH][startW];
    for (int h = 0; h < size; ++h)
    {
        for (int w = 0; w < size; ++w)
        {
            if (image[startH + h][startW + w] != reference)
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
        std::cout<<'(';
        MakeQuadTree(startH, startW, halfSize);
        MakeQuadTree(startH, startW + halfSize, halfSize);
        MakeQuadTree(startH + halfSize, startW, halfSize);
        MakeQuadTree(startH + halfSize, startW + halfSize, halfSize);
        std::cout<<')';
    }
    else
    {
        std::cout << reference;
    }
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::string inputLine;
    std::cin >> n;
    for (int h = 0; h < n; ++h)
    {
        std::cin >> inputLine;
        for (int w = 0; w < n; ++w)
        {
            image[h][w] = inputLine[w] - '0';
        }
    }

    MakeQuadTree(0, 0, n);
}
