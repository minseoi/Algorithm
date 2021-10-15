#https://www.acmicpc.net/problem/14889

from sys import stdin

N = int(input())
S = [list(map(int,stdin.readline().split())) for i in range(N)]

minimum = int(1e5)

team_Start = []
team_Link = []
def CalculateTeamPower():
    power_Start = 0
    power_Link = 0

    for i in team_Start:
        for j in team_Start:
            if i!=j:
                power_Start+=S[i][j]
    
    for i in team_Link:
        for j in team_Link:
            if i!=j:
                power_Link+=S[i][j]
    global minimum
    minimum = min(minimum, abs(power_Start-power_Link))


def SplitTeam(num, start):
    if num == 0:
        global team_Link
        team_Link = [i for i in range(N) if i not in team_Start]
        CalculateTeamPower()
    else:
        for i in range(start, N-(num-1)):
            team_Start.append(i)
            SplitTeam(num-1,i+1)
            team_Start.remove(i)
SplitTeam(N//2,0)
print(minimum)