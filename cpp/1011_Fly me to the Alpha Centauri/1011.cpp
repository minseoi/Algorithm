//https://www.acmicpc.net/problem/1011

#include <iostream>
using namespace std;

int main()
{
    int T;
    long long x, y, distance2Go;
    int jumpDistance = 1;
    int jumpCount = 0;
    cin >> T;
    
    for (int i = 0; i < T; i++)
    {
        jumpDistance = 1;
        jumpCount = 0;
        cin >> x >> y;
        distance2Go = y - x;
        while (distance2Go > jumpDistance)
        {
            if (distance2Go - (jumpDistance * 2) >= 0)
            {
                distance2Go -= (jumpDistance * 2);
                jumpCount += 2;
            }
            else
            {
                distance2Go -= jumpDistance;
                jumpCount += 1;
            }
            jumpDistance++;
        }
        if (distance2Go != 0)
            jumpCount++;
        cout << jumpCount << endl;
    }
    return 0;
}