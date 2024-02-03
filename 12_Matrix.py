matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,23,14,15]
    ]
print(matrix)

for item in matrix:
    for elem in item:
        print(elem, end="\t")
    print()
print(len(matrix)) 

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
    
import random
matrix = []
row = 4
col = 4
# for i in range(row):
#     numbers= []
#     for j in range(col):
#         numbers.append(random.randint(20,50))
#     matrix.append(numbers)
for i in range(row):
    matrix.append([random.randint(10,30) for i in range(col)])
    
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
    
summa = 0
for row in matrix:
    summa += sum(row)
    print("Res = ", sum(row))
    
print(f"Summa element of matrix : {summa}")

#Створити квадратну матрицю…кількість рядків і колонок вводить користувач з клавіатури
#Знайти суму елементів розташованих на головній та бічній діагоналі
size = 3
sum_main = 0
sum_axis = 0
matrix = []
for i in range(size):
    matrix.append([random.randint(10,30) for i in range(size)])
    
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()

for i in range(size):
    sum_main += matrix[i][i]
    sum_axis += matrix[i][size-1-i]
    
print(sum_main)
print(sum_axis)