n,x=map(int,input().split())
number=list(map(int,input().split()))
for i in range(len(number)):
    if number[i]<x:
        print(number[i], end=" ")
