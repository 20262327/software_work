a=int(input())
for i in range(a):
    c=(list(map(int,input().split())))
    print(f"{(sum(c)-c[0])/c[0]:.3f}%")