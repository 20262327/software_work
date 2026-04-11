import sys
input=sys.stdin.readline
a,b=map(int,input().split())
student={}
for i in range(b):
    number=input().rstrip()
    student[number]=i
result= sorted(student.items(), key=lambda x:x[1])
if a>len(result):
    print(*(item[0] for item in result), sep='\n')
else:
    print(*(result[i][0] for i in range(a)), sep='\n')