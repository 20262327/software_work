a,b=map(int,input().split())
hear_name=set()
see_name=set()
for i in range(a):
    hear_name.add(input())
for i in range(b):
    see_name.add(input())
total=sorted(hear_name & see_name)
print(len(total))
for j in total:
    print(j)