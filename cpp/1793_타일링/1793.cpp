//https://www.acmicpc.net/problem/1793

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string cache[251];

string AddBigInteger(const string& a, const string& b)
{
    string longNum;
    string shortNum;
    string ret = "";
    int lenA = a.size();
    int lenB = b.size();
    if(lenA > lenB)
    {
        longNum = a;
        shortNum = b;
    }
    else
    {
        longNum = b;
        shortNum = a;
    }
        
    //자릿수 맞춰주기
    int diff = abs(lenA - lenB);
    for (int i=0; i<diff; i++)
    {
        shortNum += "0";
    }
    
    int digit = longNum.size();
    bool carry = 0;
    for (int i=digit-1; i>=0; i--)
    {
        int addResult = stoi(longNum.substr(i,1)) + stoi(shortNum.substr(i,1)) + carry;
        carry = 0;
        if(addResult > 9)
        {
            carry = 1;
            addResult -= 10;
        }
        ret += to_string(addResult);
    }
    if(carry != 0)
        ret += to_string(carry);
    reverse(ret.begin(), ret.end());
    return ret;
}

string GetNumOfTiles(string n)
{
    int intN = stoi(n);
    if(cache[intN] != "")
        return cache[intN];
    
    string ret;
    string n1 = GetNumOfTiles(to_string(intN-1));
    string n2 = AddBigInteger(GetNumOfTiles(to_string(intN-2)), GetNumOfTiles(to_string(intN-2)));
    ret = AddBigInteger(n1, n2);
    cache[intN] = ret;
    return ret;
}

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n;
    
    cache[0]= "1";
    cache[1]= "1";

    while(cin>>n)
    {
        cout<<GetNumOfTiles(to_string(n))<<endl;
    }
    return 0;
}
