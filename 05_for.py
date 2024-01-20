line = 'Hyper Text Murkup language'

# print(line[0])
# print(line[1])
# print(line[2])
# print(line[3])
# print(line[4])

for letter in line:#0....last [start:end:1]
    print(letter, end="")
print()  
# for letter in line[5:10]:
#     print(letter, end="")
# print()  
# for letter in line[:5]:
#     print(letter, end="")
# print()  
# for letter in line[5:]:
#     print(letter, end="")
# print()  
# for letter in line[0:26:4]:
#     print(letter, end="")
# print()  
for letter in line[5::4]:
    print(letter, end="")
# print()    
# for num in range(0,21):#0...21
#     print(num,end=" ")
    
# print()    
for num in range(10):#0...9
    print(num,end=" ")
    
# print()    
# for num in range(10,21,2):#10..21
#     print(num,end=" ")
# print()    
# for num in range(20,10,-1):#10..21
#     print(num,end=" ")
    
#break countinue
# while True:
#     n = int(input(" 2 + 2 = ??? ---> "))
#     if n == 4:
#         break
# else:
#     print("Congratulation.....")
    
    
# print("Countinue.....")

i = 0
num = int(input("Enter number : "))  #10....0 -10

while i <= num:
    if(i%3!=0):
        print(i,end=" ")
    i+=1
while i <= num:
    if(i%3==0):
        continue
    
    print(i,end=" ")
    i+=1
    
    

