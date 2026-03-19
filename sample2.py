a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
total=[a,b,c,d,e]
for i in range(5):
    if total[i]<40:
        total[i]=40
print(sum(total)//5) 