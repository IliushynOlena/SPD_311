
# line = "Lorem ipsum dolor"
# print(line)
# print(line[0])
# print(line[-1])
# print(len(line))
# print(line[16])
# print(line[len(line)-1])
# print(line[0:5])
# print(line[:9])
# print(line[5:])
# print(line[:])
# print(line[-5:-2])
# print(line[-5:17])

# print(line[0:17:1])
# print(line[0::2])
# print(line[:9:3])
# print(line[::4])
# print(line[::-1])
numbers = '123456789'
letters = 'dslkgndklgdlksh'
line = "Lorem ipsum emet ipsum dolor ipsum gjdfkljdf ipsum kjtlekj ipsum"
word = "Fruit Apple"
word2 = "BANANA"
letterDigit= 'g121gdfgfdg12df1gdf2g'
# print('\n================= isalnum()===================')#letters and digits
# print('\t',numbers, '----->',numbers.isalnum())
# print('\t',letters, '----->',letters.isalnum())
# print('\t',line, '----->',line.isalnum())
# print('\t',word, '----->',word.isalnum())
# print('\t',word2, '----->',word2.isalnum())
# print('\t',letterDigit, '----->',letterDigit.isalnum())


# print('\n================= isalpha()===================')#only letters 
# print('\t',numbers, '----->',numbers.isalpha())
# print('\t',letters, '----->',letters.isalpha())
# print('\t',line, '----->',line.isalpha())
# print('\t',word, '----->',word.isalpha())
# print('\t',word2, '----->',word2.isalpha())
# print('\t',letterDigit, '----->',letterDigit.isalpha())

# print('\n================= isdigit()===================')#only numbers 
# print('\t',numbers, '----->',numbers.isdigit())
# print('\t',letters, '----->',letters.isdigit())
# print('\t',line, '----->',line.isdigit())
# print('\t',word, '----->',word.isdigit())
# print('\t',word2, '----->',word2.isdigit())
# print('\t',letterDigit, '----->',letterDigit.isdigit())

# login = '           '
# print('\n================= isspace()===================')#only space 
# print('\t',numbers, '----->',numbers.isspace())
# print('\t',letters, '----->',letters.isspace())
# print('\t',line, '----->',line.isspace())
# print('\t',word, '----->',word.isspace())
# print('\t',word2, '----->',word2.isspace())
# print('\t',letterDigit, '----->',letterDigit.isspace())
# print('\t',login, '----->',login.isspace())

# print('\n================= islower()===================')#only small letters
# print('\t',numbers, '----->',numbers.islower())
# print('\t',letters, '----->',letters.islower())
# print('\t',line, '----->',line.islower())
# print('\t',word, '----->',word.islower())
# print('\t',word2, '----->',word2.islower())
# print('\t',letterDigit, '----->',letterDigit.islower())

# print('\n================= isupper()===================')#only big letters
# print('\t',numbers, '----->',numbers.isupper())
# print('\t',letters, '----->',letters.isupper())
# print('\t',line, '----->',line.isupper())
# print('\t',word, '----->',word.isupper())
# print('\t',word2, '----->',word2.isupper())
# print('\t',letterDigit, '----->',letterDigit.isupper())

# print('\n================= istitle()===================')#only big letters
# print('\t',numbers, '----->',numbers.istitle())
# print('\t',letters, '----->',letters.istitle())
# print('\t',line, '----->',line.istitle())
# print('\t',word, '----->',word.istitle())
# print('\t',word2, '----->',word2.istitle())
# print('\t',letterDigit, '----->',letterDigit.istitle())

# print('\n================= lower()===================')#only big letters
# print('\t',numbers, '----->',numbers.lower())
# print('\t',letters, '----->',letters.lower())
# print('\t',line, '----->',line.lower())
# print('\t',word, '----->',word.lower())
# print('\t',word2, '----->',word2.lower())
# print('\t',letterDigit, '----->',letterDigit.lower())

# print('\n================= upper()===================')#only big letters
# print('\t',numbers, '----->',numbers.upper())
# print('\t',letters, '----->',letters.upper())
# print('\t',line, '----->',line.upper())
# print('\t',word, '----->',word.upper())
# print('\t',word2, '----->',word2.upper())
# print('\t',letterDigit, '----->',letterDigit.upper())


# print('\n================= capitalize()===================')#only big letters
# print('\t',numbers, '----->',numbers.capitalize())
# print('\t',letters, '----->',letters.capitalize())
# print('\t',line, '----->',line.capitalize())
# print('\t',word, '----->',word.capitalize())
# print('\t',word2, '----->',word2.capitalize())
# print('\t',letterDigit, '----->',letterDigit.capitalize())

# print('\n================= title()===================')#only big letters
# print('\t',numbers, '----->',numbers.title())
# print('\t',letters, '----->',letters.title())
# print('\t',line, '----->',line.title())
# print('\t',word, '----->',word.title())
# print('\t',word2, '----->',word2.title())
# print('\t',letterDigit, '----->',letterDigit.title())

# print('\n================= swapcase()===================')#only big letters
# print('\t',numbers, '----->',numbers.swapcase())
# print('\t',letters, '----->',letters.swapcase())
# print('\t',line, '----->',line.swapcase())
# print('\t',word, '----->',word.swapcase())
# print('\t',word2, '----->',word2.swapcase())
# print('\t',letterDigit, '----->',letterDigit.swapcase())

# print('\t', line, '----->',line.find('ipsum') , 'index')
# print('\t', line, '----->',line.find('ipsum',7) , 'index')
# print('\t', line, '----->',line.find('ipsum',18) , 'index')
# print('\t', line, '----->',line.find('ipsum',30) , 'index')
# print('\t', line, '----->',line.find('ipsum',46) , 'index')
# print('\t', line, '----->',line.find('ipsum',60) , 'index')

index = -1
while True:
    index = line.find('ipsum', index+1)
    if index == -1 :
        break
    print('\t',line,'---->', index)

print('\t', line, '----->',line.rfind('ipsum') , 'index')
print('\t', line, '----->',line.index('ipsum') , 'index')
print('\t', line, '----->',line.rindex('ipsum') , 'index')
print('\t', line, '----->',line.count('ipsum'), 'count' )
print('\t', line, '----->\n\t',line.replace('ipsum','yellow'))
print('\t', line, '----->\n\t',line.replace('ipsum','yellow',2))

print('\t', line, '----->',line.endswith('ipsum') )
print('\t', line, '----->',line.startswith('ipsum') )
print('\t', line, '----->',line.startswith('Lorem') )

message = "Python2024"
print(message.center(40))
print(message.center(40,'*'))
print(message.center(5))
print(message.ljust(20))
print(message.ljust(20,'@'))
print(message.ljust(5))
print(message.rjust(20))
print(message.rjust(20,'@'))
print(message.rjust(5))
message = '          Python-cool        '
print(message.lstrip())
print(message.rstrip())
print(message.strip())
message = '@#$          Python-cool        @@'
print(message.lstrip('@#$'))
print(message.rstrip('@'))
print(message.strip('@#$ '))

number = '123'
print(number.zfill(5))
number = '+123'
print(number.zfill(5))







