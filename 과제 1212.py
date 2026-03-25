a=input()
box=[]
for i in range(len(a)):
    if int(a[i])==0:
        box.append("000")
    elif int(a[i])==1:
        box.append("001")
    elif int(a[i])==2:
        box.append("010")
    elif int(a[i])==3:
        box.append("011")
    elif int(a[i])==4:
        box.append("100")
    elif int(a[i])==5:
        box.append("101")
    elif int(a[i])==6:
        box.append("110")
    elif int(a[i])==7:
        box.append("111")
answer="".join(box)
if a==0:
    print("0")
else:
    print(answer.lstrip("0"))
    
    


    
        