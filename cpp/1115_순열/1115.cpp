//https://www.acmicpc.net/problem/1115

#include <iostream>
#include <utility>
using namespace std;

//num, visited
typedef pair<int, bool> element;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int N;
    cin >> N;
    element* P = new element[N];
    int result = 0;
    
    for (int i=0; i<N; i++) {
        cin >> P[i].first;
        P[i].second = false;
    }
    
    for (int i=0; i<N; i++) {
        element* currentElement = &P[i];
        if(currentElement->second)
            continue;
        
        result++;
        do {
            currentElement->second = true;
            currentElement = &P[currentElement->first];
        } while (!currentElement->second);
    }
    if(result == 1)
        result = 0;
    cout<<result;
    
    free(P);
    P = nullptr;
}
