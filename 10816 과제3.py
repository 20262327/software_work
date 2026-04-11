n=int(input())
all_number={}
#for i in range(n):
number=list(map(int,input().split()))
for j in range(n):
    if number[j] in all_number:
        all_number[number[j]]+=1
    else:
        all_number[number[j]]=1
m=int(input())
#for i in range(m):
number_m=list(map(int,input().split()))
total=[]
for j in range(m):
    if number_m[j] in all_number:
        total.append(all_number[number_m[j]])
    else:
        total.append(0)
for i in total:
    print(i,end=' ')