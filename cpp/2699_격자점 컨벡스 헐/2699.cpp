//https://www.acmicpc.net/problem/2699

#include <iostream>
#include <vector>
#include <algorithm>

struct Point
{
    explicit Point(int _x = 0, int _y = 0) :
        X(_x),
        Y(_y)
    {}

    int X, Y {};
};

float distSqrt(const Point& p1, const Point p2)
{
    const int x = p2.X - p1.X;
    const int y = p2.Y - p1.Y;
    return x * x + y * y;
}

int ccw(const Point& p1, const Point& p2, const Point& p3)
{
    return (p2.X - p1.X) * (p3.Y - p1.Y) - (p2.Y - p1.Y) * (p3.X - p1.X);
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int P;
    std::cin >> P;
    for (int p = 0; p < P; ++p)
    {
        int N;
        std::cin >> N;
        std::vector<Point> points;
        Point inputValue;
        int startPointIndex = 0;
        for (int n = 0; n < N; ++n)
        {
            std::cin >> inputValue.X >> inputValue.Y;
            points.emplace_back(inputValue);

            if (n > 0)
            {
                if (points[n].Y == points[startPointIndex].Y)
                {
                    if (points[n].X < points[startPointIndex].X)
                    {
                        startPointIndex = n;
                    }
                }
                else if(points[n].Y > points[startPointIndex].Y)
                {
                    startPointIndex = n;
                }
            }
        }

        // 첫번째 꼭짓점을 제일 앞으로
        if (startPointIndex != 0)
        {
            std::swap(points[startPointIndex], points[0]);
        }

        // 시계방향으로 정렬
        std::sort(points.begin() + 1, points.end(),
            [points](const Point& lhs, const Point& rhs)
            {
                int ccwValue = ccw(points[0], lhs, rhs);
                if (ccwValue == 0)
                {
                    return distSqrt(points[0], lhs) < distSqrt(points[0], rhs);
                }
                return ccwValue < 0;
            }
        );

        std::vector<Point> stack {};
        stack.emplace_back(points[0]);
        stack.emplace_back(points[1]);
        for (int i = 2; i < N; ++i)
        {
            int top = stack.size();
            while (top > 1)
            {
                int ccwValue = ccw(stack[top - 2], stack[top - 1], points[i]);
                if (ccwValue >= 0)
                {
                    stack.pop_back();
                    --top;
                }
                else
                {
                    break;
                }
            }
            stack.emplace_back(points[i]);
        }

        std::cout << stack.size() << '\n';
        for (auto s : stack)
        {
            std::cout << s.X << " " << s.Y << '\n';
        }
    }
}
