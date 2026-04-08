a=int(input())
for i in range(a):
    b=[]
    num=input()
    success=True
    for j in range(len(num)):
        if num[j]=="(":
            b.append(num[j])
        elif j>0 and num[j]==")" and num[0]!=")" and len(b)!=0:
            del(b[-1])
        elif len(b)==0 and num[j]==")":
            success=False
            break
    if num[0]==")" or len(b)!=0 or success==False:
        print("NO")
    else:
        print("YES")