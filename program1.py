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

N=int(input("1보다 크고 5 이하인 N을 입력하시오:"))

A= random_matrix(N)
B= random_matrix(N)
C= random_matrix(N)

result_AB=[]
for i in range(N):
    result_AB.append([0]*N)
    
for i in range(N):
    for j in range(N):
        for k in range(N):
            result_AB[i][j]= A[i][k]*B[k][j]
for i in range(N):
    for j in range(N):
        result_AB[i][j] += C[i][j]

print_matrix(result_AB)