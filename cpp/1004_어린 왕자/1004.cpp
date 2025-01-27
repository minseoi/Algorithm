//https://www.acmicpc.net/problem/1004

#include <iostream>

struct Vector
{
    explicit Vector (const int _x = 0, const int _y = 0) :
        X(_x),
        Y(_y)
    {
    }

    int X, Y;

    static int DistSqrt(const Vector& v1, const Vector& v2)
    {
        const int x = v2.X - v1.X;
        const int y = v2.Y - v1.Y;
        return x * x + y * y;
    }

    friend std::istream& operator>>(std::istream& in, Vector& v)
    {
        in >> v.X >> v.Y;
        return in;
    }
};

struct Orbit
{
    Vector center;
    int radius;

    bool IsInPoint(const Vector& point) const
    {
        return Vector::DistSqrt(center, point) <= radius * radius;
    }

    friend std::istream& operator>>(std::istream& in, Orbit& o)
    {
        std::cin >> o.center >> o.radius;
        return in;
    }
};

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    Vector departure, destination;
    for (int t = 0; t < T; ++t)
    {
        std::cin >> departure >> destination;
        int N;
        int result = 0;
        std::cin >> N;
        Orbit o;
        for (int n = 0; n < N; ++n)
        {
            std::cin >> o;
            const bool departureIn = o.IsInPoint(departure);
            const bool destinationIn = o.IsInPoint(destination);
            if (departureIn != destinationIn)
            {
                ++result;
            }
        }
        std::cout << result << '\n';
    }
    return 0;
}
