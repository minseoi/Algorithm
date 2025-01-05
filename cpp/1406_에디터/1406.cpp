//https://www.acmicpc.net/problem/1406

#include <iostream>
#include <string>

struct CharNode
{
    const char data;

    explicit CharNode(const char data):
    data(data)
    {}

    CharNode* prev {};
    CharNode* next {};

    void SetPrev(CharNode* prevNode)
    {
        if (prevNode == nullptr)
        {
            return;
        }

        if (prev)
        {
            prev->next = prevNode;
        }
        prevNode->next = this;
        prev = prevNode;
    }

    void SetNext(CharNode* nextNode)
    {
        if (nextNode == nullptr)
        {
            return;
        }

        if (next)
        {
            next->prev = nextNode;
        }
        nextNode->prev = this;
        next = nextNode;
    }
};

struct Cursor
{
    CharNode* LChar {};
    CharNode* RChar {};
};

class Note
{
    CharNode* head {};
    Cursor cursor {};

public:
    explicit Note(const std::string& str)
    {
        head = new CharNode(str[0]);
        CharNode* current = head;
        for (int i = 1; i < str.size(); i++)
        {
            auto* newNode = new CharNode(str[i]);
            current->SetNext(newNode);
            current = newNode;
        }
        cursor.LChar = current;
        cursor.RChar = nullptr;
    }

    ~Note()
    {
        CharNode* current = head;
        while (current != nullptr)
        {
            CharNode* next = current->next;
            delete current;
            current = next;
        }
    }

    std::string GetString() const
    {
        std::string str {};
        CharNode* current = head;
        while (current != nullptr)
        {
            str.push_back(current->data);
            current = current->next;
        }

        return str;
    }

    void Input(const std::string& cmd, const char& c)
    {
        if (cmd == "L")
        {
            if (cursor.LChar != nullptr)
            {
                cursor.RChar = cursor.LChar;
                cursor.LChar = cursor.LChar->prev;
            }
        }
        else if (cmd == "D")
        {
            if (cursor.RChar != nullptr)
            {
                cursor.LChar = cursor.RChar;
                cursor.RChar = cursor.RChar->next;
            }
        }
        else if (cmd == "B")
        {
            if (cursor.LChar == head)
            {
                head = head->next;
                if (head)
                {
                    head->prev = nullptr;
                }
            }

            if (cursor.LChar != nullptr)
            {
                CharNode* targetChar = cursor.LChar;
                if (targetChar->prev)
                {
                    targetChar->prev->next = targetChar->next;
                }
                if (targetChar->next)
                {
                    targetChar->next->prev = targetChar->prev;
                }
                cursor.LChar = targetChar->prev;
                delete targetChar;
            }
        }
        else if (cmd == "P")
        {
            auto* newNode = new CharNode(c);
            if (cursor.LChar)
            {
                cursor.LChar->SetNext(newNode);
            }
            else
            {
                head = newNode;
            }

            if (cursor.RChar)
            {
                cursor.RChar->SetPrev(newNode);
            }
            cursor.LChar = newNode;
        }
    }
};

int main()
{
    std::iostream::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string initStr;
    std::cin >> initStr;
    Note note = Note(initStr);

    int numOfCmd;
    std::cin >> numOfCmd;

    char c;
    for (int i = 0; i < numOfCmd; i++)
    {
        std::string cmd;
        std::cin >> cmd;
        if (cmd == "P")
        {
            std::cin >> c;
        }
        note.Input(cmd, c);
    }
    std::cout << note.GetString();
}
