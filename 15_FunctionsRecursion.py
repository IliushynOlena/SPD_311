# line = list(map(int,input("Enter all numbers : ").split()))

# print(line)

# numbers = [2,5,8,9,6,3,1,4,785,63,25,14,22,11]
# print(numbers)
# res = list(filter(lambda x:x%2==0, numbers))
# print(res)
# res = list(filter(lambda x:x%2==1, numbers))
# print(res)
# res = list(filter(lambda x:x >= 0 and x <= 6, numbers))
# print(res)

# colors = ['red','green','blue','white','black','purple','cyan','lime']

# def checkColor(color):
#     if len(color)==4:
#         return True
#     else:
#         return False
# def checkColor(color):
#     return len(color)==4

# print(colors)
# #new_colors = list(filter(checkColor,colors)) 
# #new_colors = list(filter(lambda color:len(color)==4,colors)) 
# #new_colors = list(filter(lambda color:len(color)> 4,colors)) 
# new_colors = list(filter(lambda color:color[0]=='b',colors)) 
# print(new_colors)


# def modifyName(userName):
#     newName1 = userName.upper()
#     newName2 = userName.lower()
#     return newName1,newName2
   

# name = input("Enter your name : ")
# nameUpper, nameLower = modifyName(name)
# print(nameUpper)
# print(nameLower)


# def checkLog(userLog):
#     if userLog == 'admin':
#         return userLog.lower()
#     elif userLog == 'user':
#         return userLog.upper()
#     else:
#         return "Wrong login!"

    
# print(checkLog('admin'))
# print(checkLog('user'))
# print(checkLog('helen'))


# def showNumber(*args):
#     print(args)
    
# showNumber(1) #int  
# showNumber(1,2)#int , int
# showNumber(1,3,4,8,9)   #int,int,int,int , int
# showNumber(1,6,9,7,8,5,6,9,8) 

# def average(*args):
#     summa = 0
#     count = 0
#     for num in args :
#         #print(type(num))
#         summa+= num
#         count +=1
#     return summa/count
# #print(average(1,6,9,7,8,5,6,9,8))
# numbers = [1,6,9,7,8,5,6,9,8]#list
# print(average(*numbers))


# def show(a):
#     if a == 10:
#         return
#     print(a, "Hello")
#     show(a+1)
    
# show(1)
# print(show)
#5! = 1*2*3*4*5
#5! = 5 * 4!
#4! = 4 * 3!
#3! = 3 * 2!
#2! = 2 * 1!
#1! = 1
#0! = 0
#5 * 4 * 3 * 2 * 1
def factorial(num):#5
    if num == 1:
        return 1
    print(num)
    return num* factorial(num-1)

print(factorial(5))


    
      
    