

def show(color):
    print(color)
def summa(a,b):
    return a+b    
print(summa(5,5))
show("green")

lambda_show = lambda color:print(color)
lambda_show("red")
print(show)
print(lambda_show)

lambda_sum = lambda a,b: a+b   
print(lambda_sum(5,8))

def modifyList(list):
    for i in range(len(list)):
        list[i] = list[i]*2

numbers = [10,5,8,9,6,3,11,4]
print(numbers)
modifyList(numbers)
print(numbers)
# def double(x):
#     return x*2
# def pow(x):
#     return x**2
# def inrement(x):
#     return x+1
# def decrement(x):
#     return x-1
#res = list (map(double, numbers))
res = list (map(lambda x:x*2, numbers))
print(res)
#res = list (map(pow, numbers))
res = list (map(lambda x:x**2, numbers))
print(res)
#res = list (map(inrement, numbers))
res = list (map(lambda x:x+1, numbers))
print(res)
#res = list (map(decrement, numbers))
res = list (map(lambda x:x-1, numbers))
print(res)