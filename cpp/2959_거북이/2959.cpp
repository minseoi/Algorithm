//https://www.acmicpc.net/problem/2959

#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int sides[4];
    for (int i=0; i<4; i++) {
        cin>>sides[i];
    }
    
/* Selection Sorting Begin */
    for (int i=0; i<3; i++) {
        int minValueIndex = i;
        for (int j=i+1; j<4; j++) {
            minValueIndex = sides[j]<sides[minValueIndex]? j:minValueIndex;
        }
        if(minValueIndex != i)
        {
            sides[i] ^= sides[minValueIndex];
            sides[minValueIndex] ^= sides[i];
            sides[i] ^= sides[minValueIndex];
        }
    }
/* Selection Sorting End */
    
    cout<<sides[0] * sides[2];
}
