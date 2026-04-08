a=int(input())
c=[]
b=list(map(int,input().split()))
b.sort()
for i in range(a):
    c.append(b[i]*i-b[i]*(a-i))
print(sum(c))
        