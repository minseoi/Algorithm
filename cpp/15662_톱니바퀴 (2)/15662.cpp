//https://www.acmicpc.net/problem/15662

#include <iostream>
#include <string>

class Gears
{
private:
	class Gear
	{
	private:
		int sawtooth[8];
	public:
		void Initialize(const std::string& s);
		int GetRightSawtooth();
		int GetLeftSawtooth();
		int GetUpSawtooth();
		void Rotate(int dir);
	};
	Gear *gears;
	int size;
public:
	Gears(int size);
	void InitGear(int idx, const std::string& s);
	void RotateGear(int idx, int dir, const char& flow = 'N');
	int GetNumberOfS12Gears();
};

void Gears::Gear::Initialize(const std::string& s)
{
	for (int i = 0; i < s.length(); i++)
	{
		sawtooth[i] = s[i] - 48;
	}
}

int Gears::Gear::GetLeftSawtooth()
{
	return sawtooth[6];
}

int Gears::Gear::GetRightSawtooth()
{
	return sawtooth[2];
}

int Gears::Gear::GetUpSawtooth()
{
	return sawtooth[0];
}

void Gears::Gear::Rotate(int dir)
{
	int temp;
	switch (dir)
	{
	case -1://반시계 방향
		temp = sawtooth[0];
		for (int i = 0; i < 7; i++)
			sawtooth[i] = sawtooth[i+1];
		sawtooth[7] = temp;
		break;
	case 1://시계 방향
		temp = sawtooth[7];
		for (int i = 7; i > 0; i--)
			sawtooth[i] = sawtooth[i - 1];
		sawtooth[0] = temp;
		break;
	}
}

Gears::Gears(int size):size(size)
{
	gears = new Gear[size];
}

void Gears::InitGear(int idx, const std::string& s)
{
	gears[idx].Initialize(s);
}

void Gears::RotateGear(int idx,int dir, const char& flow)
{
	//L flow
	if (0 <= idx - 1 && flow != 'R')
	{
		if(gears[idx].GetLeftSawtooth() != gears[idx-1].GetRightSawtooth())
			RotateGear(idx - 1, dir*-1, 'L');
	}

	if (idx + 1 < size && flow != 'L')
	{
		if (gears[idx].GetRightSawtooth() != gears[idx+1].GetLeftSawtooth())
			RotateGear(idx + 1, dir*-1, 'R');
	}
	gears[idx].Rotate(dir);
}

int Gears::GetNumberOfS12Gears()
{
	int result = 0;
	for (int i = 0; i < size; i++)
	{
		if (gears[i].GetUpSawtooth() == 1)
			result++;
	}
	return result;
}

int main()
{
	int T;
	std::string input;
	std::cin >> T;
	Gears Gs(T);
	for (int i = 0; i < T; i++)
	{
		std::cin >> input;
		Gs.InitGear(i, input);
	}

	int K;
	int gearNum, dir;
	std::cin >> K;
	for (int i = 0; i < K; i++)
	{
		std::cin >> gearNum >> dir;
		gearNum--;
		Gs.RotateGear(gearNum, dir);
	}

	int result = Gs.GetNumberOfS12Gears();
	std::cout << result << std::endl;
	return 0;
}