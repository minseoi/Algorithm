//https://www.acmicpc.net/problem/1708

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

    static long long distSqrt(const Point& p1, const Point p2)
    {
        const long long x = p2.X - p1.X;
        const long long y = p2.Y - p1.Y;
        return x * x + y * y;
    }
};

class PointSet
{
    std::vector<Point> m_points;

public:
    explicit PointSet() = default;

    void AddPoint(const Point& _newPoint)
    {
        m_points.emplace_back(_newPoint);
    }

    std::vector<Point> CalculateConvexHull()
    {
        std::vector<Point> ret {};

        int startPointIndex = 0;
        const int size = m_points.size();
        for (int i = 1; i < size; ++i)
        {
            const Point& startPoint = m_points[startPointIndex];
            const Point& candidate = m_points[i];
            if ((candidate.Y < startPoint.Y) ||
                (candidate.Y == startPoint.Y && candidate.X < startPoint.X))
            {
                startPointIndex = i;
            }
        }
        std::swap(m_points[0], m_points[startPointIndex]);

        std::sort(m_points.begin() + 1, m_points.end(),
    [this](const Point& lhs, const Point& rhs)
        {
            long long ccwValue = Ccw(m_points[0], lhs, rhs);
            if (ccwValue == 0)
            {
                return Point::distSqrt(m_points[0], lhs) < Point::distSqrt(m_points[0], rhs);
            }
            return ccwValue > 0;
        }
        );

        ret.emplace_back(m_points[0]);
        ret.emplace_back(m_points[1]);
        for (int i = 2; i < size; ++i)
        {
            int top = ret.size();
            while (top >= 2)
            {
                long long ccwValue = Ccw(ret[top - 2], ret[top - 1], m_points[i]);
                if (ccwValue <= 0)
                {
                    ret.pop_back();
                    --top;
                }
                else
                {
                    break;
                }
            }
            ret.emplace_back(m_points[i]);
        }
        return ret;
    }

private:
    static long long Ccw(const Point& p1, const Point& p2, const Point& p3)
    {
        return 1LL * (p2.X - p1.X) * (p3.Y - p1.Y) - 1LL * (p2.Y - p1.Y) * (p3.X - p1.X);
    }
};

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    PointSet pointSet;
    Point inputValue;
    for (int n = 0; n < N; ++n)
    {
        std::cin >> inputValue.X >> inputValue.Y;
        pointSet.AddPoint(inputValue);
    }
    std::vector<Point> convexHull = pointSet.CalculateConvexHull();
    std::cout << convexHull.size();
}
