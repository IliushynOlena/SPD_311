# a = None 
# b = None
# while a == None or b == None or b == 0:
#     try:
#         a = int(input("Enter number a: "))
#         b = int(input("Enter number b: "))
        
#         print(a/b)
    
#     except ValueError:
#         print("You need to enter number!!!")
#     except ZeroDivisionError:
#         print("You can*t divide by zero!!!")
#     except NameError:
#         print("NameError ") 
#     except Exception:
#         print("Some error") 


# print("Continue........End!!! ")
# try:
#     age = int(input("Enter age : "))
#     if age < 0 :
#         raise Exception("Age error. Age < 0")
#     if age > 130:
#         raise Exception("Age error. Age > 130")
#     print("Age = " ,age)
# except ValueError:
#     pass
#     #print("Value error")
# except Exception as ex:
#     print(ex, type(ex).__name__)
# else:
#     print("Good!!!")
# finally:
#     print("Finally!!!!")
    
colors = ['red','green','blue','white']
try:
    index = int(input("Enter age : "))
    print(colors[index])
except IndexError:
    print("Index was out of range")