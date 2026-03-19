a,b=map(int,input().split())
if a>b:
    big=a
    small=b
else:
    big=b
    small=a
    sum=0
    for i in range(small,big+1):
        sum+=i
    print(sum)
    
    