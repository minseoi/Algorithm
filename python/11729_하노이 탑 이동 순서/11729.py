#https://www.acmicpc.net/problem/11729

N= int(input())
movingList = []
count = 0

def Hanoi(start,end,sub,num):
    global count
    if num == 1:
        movingList.append((start,end))
        count += 1
    else:
        Hanoi(start,sub,end,num-1)
        Hanoi(start,end,sub,1)
        Hanoi(sub,end,start,num-1)

Hanoi(1,3,2,N)
print(count)
for i in movingList:
    print(i[0],i[1])