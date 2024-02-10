# a = 5


# def showMessage():
#     b = 100
#     print(f"variable a in function {a}")
#     print(f"variable b in function {b}")
#     print("Hello")
   

# print(showMessage) 
    
# showMessage()
# showMessage()
# showMessage()
# showMessage()
# showMessage()
# showMessage()

# print(f"variable in main {a}")

# def showMessageToUser(name):
#     print(f"Hello, {name}")
   
# nameUser = input("Enter your name : ") 
# showMessageToUser(nameUser)
# showMessageToUser("Denus")
# showMessageToUser("Olga")

# def summa(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def multy(a,b):
#     return a*b

# def div(a,b):
#     if b == 0:
#         return#break
#     return a/b

# def calculator(a,b,op):
#     if op == '+':
#         return summa(a,b)
#     if op == '-':
#         return sub(a,b)
#     if op == '*':
#         return multy(a,b)
#     if op == '/':
#         return div(a,b)
    
# def getOperation(line):
#     if line.find('+') != -1:
#         return '+'
#     if line.find('-') != -1:
#         return '-'
#     if line.find('*') != -1:
#         return '*'
#     if line.find('/') != -1:
#         return '/'
    
# example = input("Enter your example ( 2 + 2 )---> ")# 7 - 4 
# operation = getOperation(example)

# num1 = float(example.split(operation)[0]) 
# num2 = float(example.split(operation)[1]) 
# print(num1, num2)
# res = calculator(num1,num2,operation)
# print(f"Res = {res}")

# print(f"Summa {summa(5,8)}")
# res = summa(15,9)
# print(f"Res = {res}")
# summa(1,1)
# summa(2,2)
# summa(7,4)

# import random
# def fillList(list1, count = 10, min = 1, max = 10):
#     return [random.randint(min,max) for i in range(count)]
    
    
# numbers = []
# print(numbers)
# numbers = fillList(numbers)#count = 10, min = 1, max = 10
# print(numbers)
# numbers = fillList(numbers, 20)#count = 20, min = 1, max = 10
# print(numbers)
# numbers = fillList(numbers, 30, 5)#count = 30, min = 5, max = 10
# print(numbers)
# numbers = fillList(numbers, 30, 5,80)#count = 30, min = 5, max = 80
# print(numbers)


def SummaAllNumber( start, end, *args):
    print(f"Start = {start}")
    print(f"End = {end}")
    #args[0] = 1000 # error
    for elem in args:
        print(elem, end=" ")
    print()   
    # print(f"Element index [0] = {args[0]}")
    # print(f"Element index [last] = {args[-1]}")
    # print(f"Len = {len(args)}")
    # print(f"Count element [5]  = {args.count(5)}")
    # print(f"Index element [5]  = {args.index(5)}")
    # print(f"Element index [last] = {args[len(args)-1]}")
    # temp = list(args)

    return sum(args)

print(SummaAllNumber(1,23,4,5,6,7,8,9,3,6,9,5,7))
