//https://www.acmicpc.net/problem/1116

#include <iostream>
#include <utility>
using namespace std;

//num, graphGroupID
typedef pair<int, int> element;

void ChangeGroupID(element* array, const int arrayLength, const int source, const int target)
{
    for (int i=0; i<arrayLength; i++) {
        if(array[i].second == source)
            array[i].second = target;
    }
}

int FindMinimum(const element* array, const int arrayLength, const int ignoreGroupID, const int targetIndex)
{
    int minIndex = targetIndex;
    for(int i=0;i<arrayLength;i++) {
        if(array[i].first < array[minIndex].first && array[i].second != ignoreGroupID)
        {
            minIndex = i;
        }
    }
    minIndex = minIndex==targetIndex?-1:minIndex;
    return minIndex;
}

int FindMinimum(const element* array, const int arrayLength, const int ignoreGroupID)
{
    bool isFind = false;
    int minIndex = -1;
    for(int i=0;i<arrayLength;i++) {
        if(array[i].second != ignoreGroupID)
        {
            isFind = true;
            if(minIndex == -1)
            {
                minIndex = i;
                continue;
            }
            else
            {
                if(array[i] < array[minIndex])
                {
                    minIndex = i;
                }
            }
        }
    }
    if(isFind)
        return minIndex;
    else return -1;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int N;
    cin >> N;
    element* P = new element[N];
    
    for (int i=0; i<N; i++) {
        cin >> P[i].first;
        P[i].second = -1;
    }
    
/* Groupping Begin */
    int currentGroupID = 0;
    for (int i=0; i<N; i++) {
        element* currentElement = &P[i];
        if(currentElement->second != -1)
            continue;
        
        ++currentGroupID;
        do {
            currentElement->second = currentGroupID;
            currentElement = &P[currentElement->first];
        } while (currentElement->second == -1);
    }
/* Groupping End */
    
    // ex) 닫힌 그래프가 4개면 Swap은 3번을 해야 한다.
    int SwapMaxCount = currentGroupID - 1;
    
    if(SwapMaxCount != 0)
    {
        int candidateSourceIndex = -1;
        int swapSourceIndex = -1;
        int swapTargetIndex = -1;

        //사전적으로 가장 앞서는 자식 순열을 출력해야 하기 때문에
        //1그룹 0부터 방향대로 돌면서 최대한 앞쪽에서 스왑가능한 인덱스 찾기
        int searchIndex = 0;
            do {
            swapTargetIndex =FindMinimum(P, N, 1, searchIndex);
            candidateSourceIndex = searchIndex;
            if(swapTargetIndex != -1)
            {
                swapSourceIndex = searchIndex;
                break;
            }
            searchIndex = P[searchIndex].first;
            } while (searchIndex != 0);
        if(swapSourceIndex == -1)
        {
            swapSourceIndex = candidateSourceIndex;
            swapTargetIndex = FindMinimum(P, N, 1);
        }
        
        
        for (int i=0; i<SwapMaxCount; i++) {
            ChangeGroupID(P, N, P[swapTargetIndex].second, 1);
            
            element temp;
            temp = P[swapTargetIndex];
            P[swapTargetIndex] = P[swapSourceIndex];
            P[swapSourceIndex] = temp;
            swapSourceIndex = swapTargetIndex;
            swapTargetIndex = FindMinimum(P, N, 1);
        }
    }
    
    for (int i=0; i<N; i++) { cout<<P[i].first << " "; }
    
    free(P);
    P = nullptr;
}
