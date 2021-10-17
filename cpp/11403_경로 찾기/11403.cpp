//https://www.acmicpc.net/problem/11403

#include <iostream>
using namespace std;

int N;
int** matrix;
int *visited;

void dfs(int start)
{
    visited[start] = 1;
    for (int _c = 0; _c < N; _c++)
        if(matrix[start][_c] == 1 && visited[_c] == 0)
            dfs(_c);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin>>N;
    visited = new int[N];
    matrix = new int*[N];
    for (int i = 0; i < N; i++)
        matrix[i] = new int[N];
    
    /*인접행렬 입력*/
    for (int r = 0; r < N; r++)
        for (int c = 0; c < N; c++)
            cin>>matrix[r][c];
    
    for (int r = 0; r < N; r++)
    {
        /*visited 초기화*/
        for (int i = 0; i < N; i++)
            visited[i] = 0;

        for (int c = 0; c < N; c++)
        {
            if(matrix[r][c] == 1)
                dfs(c);
        }
        
        for (int i = 0; i < N; i++)
        {
            if(visited[i] == 1)
                matrix[r][i] = 1;
        }
    }
    
    for (int r = 0; r < N; r++)
    {
        for (int c = 0; c < N; c++)
            cout<<matrix[r][c]<<' ';
        cout<<'\n';
    }
}