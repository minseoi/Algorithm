#https://www.acmicpc.net/problem/2875

N, M, K = map(int,input().split())

count =0
while N>=2 and M>=1 and N+M >= K+3:
    N-=2
    M-=1
    count+=1
    
print(count)
