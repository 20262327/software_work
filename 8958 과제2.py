a=int(input())
for i in range(a):
    c=0
    b=input()
    combo=0
    for e in range(len(b)):
        if b[e]=="X":
            c=c
            combo=0
        else:
            c=c+combo+1
            combo+=1
    print(c)
            
            