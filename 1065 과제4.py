def d(n):
    n=str(n)
    total=[]
    if int(n)>99:
        if int(n)==1000:
            return total
        for i in range(len(n)-2):
            if int(n[i])-int(n[i+1])==int(n[i+1])-int(n[i+2]):
                total.append(int(n))
    else:
        total.append(int(n))
    return total
a=int(input())
b=[]
for i in range(1,a+1):
    if len (d(i))>0:
        b.append(i)
print(len(b))  