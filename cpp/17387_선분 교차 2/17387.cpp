//https://www.acmicpc.net/problem/17387

#include <iostream>

struct Vector
{
    long long X, Y {};

    explicit Vector (const long long x = 0, const long long y = 0) :
    X(x),
    Y(y)
    {
    }

    friend Vector operator-(const Vector& lhs, const Vector& rhs)
    {
        return Vector(lhs.X - rhs.X, lhs.Y - rhs.Y);
    }

    friend bool operator>(const Vector& lhs, const Vector& rhs)
    {
        if (lhs.X != rhs.X)
        {
            return lhs.X > rhs.X;
        }
        if (lhs.Y > rhs.Y)
        {
            return true;
        }
        return false;
    }

    static long long Cross(const Vector& v1, const Vector& v2)
    {
        return (1LL * v1.X * v2.Y) - (1LL * v1.Y * v2.X);
    }

    static long long CCW(const Vector& p1, const Vector& p2, const Vector& p3)
    {
        return Cross(p2 - p1, p3 - p2);
    }

    static int NormalizeCCW(const Vector& p1, const Vector& p2, const Vector& p3)
    {
        long long ccw = CCW(p1, p2, p3);
        if (ccw > 0)
        {
            return 1;
        }
        if (ccw < 0)
        {
            return -1;
        }
        return 0;
    }
};

struct LineSegment
{
    Vector A;
    Vector B;
};

bool IsIntersect(const LineSegment& L1, const LineSegment& L2)
{
    const int L1L2 = Vector::NormalizeCCW(L1.A, L1.B, L2.A) * Vector::NormalizeCCW(L1.A, L1.B, L2.B);
    const int L2L1 = Vector::NormalizeCCW(L2.A, L2.B, L1.A) * Vector::NormalizeCCW(L2.A, L2.B, L1.B);
    if (L1L2 > 0 || L2L1 > 0)
    {
        return false;
    }

    if (L1L2 == 0 && L2L1 == 0)
    {
        LineSegment copiedL1 = L1;
        LineSegment copiedL2 = L2;
        if (L1.A > L1.B)
        {
            std::swap(copiedL1.A, copiedL1.B);
        }
        if (L2.A > L2.B)
        {
            std::swap(copiedL2.A, copiedL2.B);
        }

        if (copiedL1.A > copiedL2.B || copiedL2.A > copiedL1.B)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    LineSegment L1, L2;
    std::cin >> L1.A.X >> L1.A.Y >> L1.B.X >> L1.B.Y;
    std::cin >> L2.A.X >> L2.A.Y >> L2.B.X >> L2.B.Y;
    std::cout << (IsIntersect(L1, L2) ? 1 : 0);
    return 0;
}
