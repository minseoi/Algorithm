//https://www.acmicpc.net/problem/10828

#include <iostream>
#include <string>

#define STACK_SIZE 10000
template <typename T>
class Stack
{
    T stack[STACK_SIZE] {};
    int size {};

public:
    void Push(int n)
    {
        if (IsFull())
        {
            return;
        }

        stack[size] = n;
        size = std::min(size + 1, STACK_SIZE);
    }

    int Pop()
    {
        if (IsEmpty())
        {
            return -1;
        }

        const int ret = Top();
        size = std::max(size - 1, 0);
        return ret;
    }

    int Top()
    {
        if (IsEmpty())
        {
            return -1;
        }

        return stack[size - 1];
    }

    int GetSize() const
    {
        return size;
    }

    bool IsFull() const
    {
        return size >= STACK_SIZE;
    }

    bool IsEmpty() const
    {
        return size <= 0;
    }
};

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    Stack<int> stack;
    int n, arg;
    std::string cmd;
    std::cin >> n;
    for (int i = 0; i < n; ++i)
    {
        std::cin >> cmd;

        if (cmd == "push")
        {
            std::cin >> arg;
            stack.Push(arg);
        }
        else if (cmd == "pop")
        {
            std::cout << stack.Pop() << '\n';
        }
        else if (cmd == "size")
        {
            std::cout << stack.GetSize() << '\n';
        }
        else if (cmd == "empty")
        {
            std::cout << (stack.IsEmpty() ? 1 : 0) << '\n';
        }
        else if (cmd == "top")
        {
            std::cout << stack.Top() << '\n';
        }
    }
}
