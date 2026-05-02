import random

def random_matrix(N):
    matrix=[]
    max_val=N*N*10
    for i in range(N):
        semi_matrix=[]
        for j in range(N):
            num=random.randint(1,max_val-1)
            semi_matrix.append(num)
        matrix.append(semi_matrix)
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()        

N=int(input("1초과 5이하의 자연수 n을 입력하시오:"))
A=random_matrix(N)

trans_matrix=[]
for i in range(N):
    trans_matrix.append([0]*N)
for i in range(N):
    for j in range(N):
        trans_matrix[i][j]=A[j][i]

print_matrix(A)
print_matrix(trans_matrix)