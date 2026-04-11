a=int(input())
b=set()
for i in range(a):
    name,status=input().split()
    if status=="enter":
        b.add(name)
    else:
        b.discard(name)
b=sorted(b,reverse=True)

for i in range(len(b)):
    print(b[i])
        
    