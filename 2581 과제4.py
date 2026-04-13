def d(n):
    total=set()
    if n==2:
        total.add(n)
        return total
    for i in range(2,n):
        if n%i==0 and n in total:
            total=set()
            break            
        elif n%i==0 and n not in total:
            break
        else:
            total.add(n)
    total=sorted(total)
    return total
m=int(input())
n=int(input())
all_number=[]
for j in range (m,n+1):
    all_number.extend(d(j))
if sum(all_number)==0:
    print(-1)
else:
    print(sum(all_number))
    print(min(all_number))