#open file
#read file
#write file 
#close file
# url = r'C:\Users\helen\Desktop\SPD_311\WorkWithFile\myfile.txt'
# #file = open('WorkWithFile/myfile.txt')
# file = open(url,'r')
# #print(file.read())
# #print(file.readline().strip())
# #print(file.readlines())
# print(file.read(5))
# file.close()

# with open(url) as file:
#     line = file.read()
#     print(type(line))
#file.close()

# url = 'WorkWithFile/write.txt'
# with open(url,'a') as file:
#     file.write("Have a nice day!!!\n")
    
# url = 'WorkWithFile/write.txt'
# with open(url,'w') as file:
#     file.write("")


# lines = [
#     'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
#     'Quisque aliquet tellus eget aliquam porttitor.',
#     'Sed non turpis ac lacus facilisis mollis.',
#     'Proin nec nisl eget dolor luctus luctus vel quis urna.'
# ]
# url = 'WorkWithFile/write.txt'
# with open(url,'w') as file:
#     file.writelines(lines)
    # counter = 1
    # ##file.write(lines)
    # for line in lines:
    #     file.write(f"{counter}. {line}\n")
    #     counter+=1
# def readFile(fname):
#     with open(fname,'r') as file:
#         return file.read()
    
# def appFile(fname,info):
#     with open(fname,'a') as file:
#         file.write(info)
    
def readCollection(fname):
    with open(fname,'r') as file:
        return file.readlines()
url = 'WorkWithFile/write.txt'
url2 = 'WorkWithFile/myfile.txt'
# text = readFile(url2)
# appFile(url, text)

# line=[]
# line = readCollection(url)
# with open(url2,'w') as file:
#     for l in line[::-1]:
#         #print(l.strip())
#         file.write(l.strip()+ "\n")
a = 5
with open(url,'a') as file:
    file.write(str(a))
    # print(file.readable())
    # print(file.writable())