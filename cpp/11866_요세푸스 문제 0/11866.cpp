//https://www.acmicpc.net/problem/11866

#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n, k= 0;
    std::cin>>n>>k;
    
    bool* validCheckList = new bool[n];
    
    for(int i = 0; i<n; i++)
    {
        validCheckList[i] = true;
    }
    int validCount = 0;
    int currentIndex = 0;
    
    int* resultList = new int[n];
    
    for(int i = 0; i<n; ++i)
    {
        validCount = 0;
        while (validCount < k)
        {
            if(validCheckList[currentIndex])
                ++validCount;
                
            if(validCount < k)
                currentIndex = ++currentIndex % n;
        }
        validCheckList[currentIndex] = false;
        resultList[i] = currentIndex+1;
    }
    
    cout<<"<";
    for (int i = 0; i<n; i++)
    {
        cout<<resultList[i];
        if(i != n-1)
            cout<<", ";
    }
    cout<<">";
    
    free(validCheckList);
    free(resultList);
}
