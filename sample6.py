list=["월","화","수","목","금","토","일"]
today=input()
today2=list.index(today)
a=int(input("며칠뒤가 궁금해?"))
print(list[(today2+a)%7])
#a,b=map(int,input().split())
#print[list]