def not_self(n):
    b=[]
    for i in str(n):
        b.append(int(i))
    c=sum(b)+n
    return c
total=set()
all_number=set()
for j in range(1,10001):
    total.add(not_self(j))
    all_number.add(j)
want=all_number-total
for i in sorted(want):
    print(i)