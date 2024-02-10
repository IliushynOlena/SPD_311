line = "Hello"

mark = 12# number - int
sum = 0
count = 10
for i in range(count):
    mark = int(input(f"Enter {i+1} mark : "))
    sum+= mark
    
print(f"Average mark = {sum/count}")
#find max and min
category = ["Drama","Comedy","Fantasy","Melodrama","Adventure"]
marks = [12,11,7,8,9,3,6,5,4,5,12]
courses = list(("Math","Databases","Python","C++"))
arr = []
new_arr = list()
myCourses = ["Algorithms",2345,7009,"Networks",[12,5,7,8,9,6]]
mySymbols = list('asdfghjkl')
print(category)
print(marks)
for mark in marks:
    print(f"Mark = {mark}")

print(courses)
print(arr)
print(new_arr)
print(myCourses)
print(mySymbols)

list_1 = [i*i for i in range(6)]
print(list_1)
for i in range(6):
    print(i, end=" ")
print()  
import random
numbers = [random.randint(10,30) for i in range(10)]
print(numbers)
summa_minus_numbers= 0
symbols = [i for i in 'example']
print(symbols)

print("_".join(symbols))

line = "blue green yellow orange purple black white broun"
list_colors = line.split(" ")
print(list_colors)
for color in list_colors:
    print(color, end=" ")
    
print()    
list2 = [i*5 for i in "abcdefg"]
print(list2)

list3 = [i*i for i in range(1,11) if i%2== 0]
print(list3)

customers = ["Bob", "Anna","Joe","Bob", "Anna","Nick"]
print(customers)
list4 = [i for i in customers if i != "Bob" and i != "Joe"]
print(list4)

line = "Hello world"
print(line[0])
print(line[0:8])
print(customers[0])
print(customers[1])
print(customers[2])
print(customers[-1])
print(customers[len(customers)-1])
print(customers[0:3])
print(customers[:-1])
print(customers[2:])
print(customers[::2])
print(customers[::-1])
print(customers)
customers[0]= "Ivanka"
print(customers)
marks = [12,11,7,8,9,3,6,5,4,5,12, 1]
print(f"Legth = {len(marks)}")
print(f"Max = {max(marks)}")
print(f"Min = {min(marks)}")
print(f"Summa = {sum(marks)}")
print(f"Sorted = {sorted(marks)}")
print(marks)
for mark in marks:
    print(mark, end=" ")
print()
for i in range(len(marks)):
    print(marks[i], end= " ")
print()   
colors = ["red", "green","blue"]
print(colors)
colors.append("orange")
print(colors)
colors2 = ["black","white","broun"]
colors.extend(colors2)
print(colors)
colors.insert(1,"purple")
print(colors)
colors.insert(-1,"purple")
print(colors)
colors.insert(5,"purple")
print(colors)
colors.remove("purple")
print(colors)
colors.pop()#delete last element
print(colors)
colors.pop(5)#delete  element by index
print(colors)
start = 0
for i in range(len(colors)):
    start = colors.index('purple', start+1)
    print(f"Element purple find in index [{start}]")
    
print(f'Count of word purple = {colors.count("purple")}')
print(sorted(colors))
print("-------------------------------------------")
print(colors)
colors.sort(reverse=True)
print(colors)

colors.reverse()
print(colors)
for i in range(len(colors)):
    if colors[i] == "purple":
        print(f"Index element purple = [{i}]")

colors.clear()
print(colors)

    
