//https://www.acmicpc.net/problem/18258

#include <iostream>
using namespace std;

class Queue
{
    int* queue = new int[2000000];
    int front=0, back=0;

    public:
        void Push(int);
        int Pop();
        int Size();
        bool Empty();
        int Front();
        int Back();
};

void Queue::Push(int num)
{
    queue[back++] = num;
}

int Queue::Pop()
{
    if(Empty())
        return -1;
    else
        return queue[front++];
}

int Queue::Size()
{
    return back-front;
}

bool Queue::Empty()
{
    if(Size() == 0)
        return true;
    else
        return false;
}

int Queue::Front()
{
    if(Empty())
        return -1;
    else
        return queue[front];
}

int Queue::Back()
{
    if(Empty())
        return -1;
    else  
        return queue[back-1];
}

int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
	cout.tie(NULL);

    Queue queue;
    int N;
    cin>>N;
    string command;
    for (int i = 0; i < N; i++)
    {
        cin>>command;
        if(command == "push")
        {
            int inputNum;
            cin>>inputNum;
            queue.Push(inputNum);
        }
        else if(command == "pop")
        {
            cout<<queue.Pop()<<"\n";
        }
        else if(command == "size")
        {
            cout<<queue.Size()<<"\n";
        }
        else if(command == "empty")
        {
            cout<<queue.Empty()<<"\n";
        }
        else if(command == "front")
        {
            cout<<queue.Front()<<"\n";
        }
        else if(command == "back")
        {
            cout<<queue.Back()<<"\n";
        }
    }
    return 0;
}