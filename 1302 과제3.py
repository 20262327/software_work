a=int(input())
b={}
for i in range(a):
    title=input()
    if title in b:
        b[title]+=1
    else:
        b[title]=1
c=max(b.values())
d=[]
for title in b:
    if b[title]<c:
        pass
    else:
        d.append(title)
d.sort()
for i in d:
    print(i)
        
    