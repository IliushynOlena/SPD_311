
# money = float(input("Enter money :"))
# grn = int(money//1) 
# coins = int(money%1*100) 
# print(f'Grn : {grn} . coins : {coins}')
# print(grn, money)
# print("Grn : {}. Coins {}".format(grn ,coins))

# a,b,c = 1 ,3,8 
# print(a ,b ,c)

# a = b = c = 10# <====
# print(a ,b ,c)
# var= 5
# print(var)

# var = 100
# 5 == 6  4 != 8 > < >= <= 
# print("1 == 1" , 1 == 1)  #True
# print("1 != 1" , 1 != 1)  #False
# print("1 != 2" , 1 != 2)  #True
# print("1 != 1" , 1 != 1)  #False
# print("1 > 8" , 1 > 8)  #
# print("1 < -5" , 1 < -5)  #
# print("9 >= 9" , 9 >= 9)  #
# print("9 <= 12" , 9 <= 12)  #

# print(bool(""))
# print(bool(0))
# print(bool(0.0))
# print(bool(None))
# print(bool("It Step Academy"))
# print(bool(1))

# #and
# competent = True
# responsible = True
# print(competent and responsible)

# #or - abo
# competent = False
# responsible = False
# print(competent or responsible)

# #not
# competent = True
# print(not competent )

# age = int(input("Enter age : "))
# if age >= 18 and age <= 120:
#     print("Ok")
# else:
#     print("Error age")
    
# if 18 <= age <= 120:
#     print("Ok")
# else:
#     print("Error age")
# day = int(input("Enter day : "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else :
#     print("Error day")

# login = input("Enter login : ")
# if login == "admin":
#     password = input("Enter password : ")
#     if(password == "step"):
#         print("Welcome!!!!")
#     else:
#         print("Error password!!!")    
# elif login == "exit":
#     print("Exit")
# else:
#     print("Login error")


# import math
# print(math.ceil(2.5))#3.0
# print(math.floor(2.5))#2.0
# print(math.pow(2 ,5))#2.0
# print(math.sqrt(64))#2.0

# import random

# print(random.random())#0...1
# print(random.randint(1,5))#0...5
# print(random.randint(100,200))#100...200
# print(random.randint(10,20))#10...20

# Уявіть, що ви прийшли в магазин, де продають магічні карамельки
# по 270 монет за 1 кг. Зараз у магазині проходить акція: 
# при покупці більше, ніж 500 г карамелек, 
# їхня вартість дорівнює 200 монетам за 1 кг..

# price_1 = 270
# price_2 = 200
# gramm = int(input("Enter weight (gram) : "))
# kg = gramm/1000
# print(f"Your candy weight is : {kg} kg")
# if kg < 0.5:
#     total = kg * price_1
# else :
#     total = kg * price_2
# total = math.ceil(total)
# print(f"You have to pay : {total} coins. ")
day = int(input("Enter day : "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else :
    print("Error day")
# if vs match
day = int(input("Enter day : "))#key 7
#key = input("Enter day : ")
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Error day")

        
