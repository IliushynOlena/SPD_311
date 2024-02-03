email = 'skdfsdkjghkjds@gmail.com'
phone= '+38054646879879'

import re   #regular expresion , regex, RE

str_1 = '380974589335'
str_2 = '234'
str_3 = 'Lorem 21 ipsum red'



# print('\t',str_1,'------->', re.search('1',str_1))
# print('\t',str_2,'------->', re.search('1',str_2))
# print('\t',str_3,'------->', re.search('1',str_3))

# print('\t',str_1,'------->', re.search('12',str_1))
# print('\t',str_2,'------->', re.search('12',str_2))
# print('\t',str_3,'------->', re.search('12',str_3))

# print('\t',str_1,'------->', re.search('[12]',str_1))
# print('\t',str_2,'------->', re.search('[12]',str_2))
# print('\t',str_3,'------->', re.search('[12]',str_3))

# print('\t',str_1,'------->', re.search('[1-9]',str_1))
# print('\t',str_2,'------->', re.search('[1-9]',str_2))
# print('\t',str_3,'------->', re.search('[1-9]',str_3))

# print('\t',str_1,'------->', re.search('[a-z]',str_1))
# print('\t',str_2,'------->', re.search('[a-z]',str_2))
# print('\t',str_3,'------->', re.search('[a-z]',str_3))
# print('\t',str_3,'------->', re.search('[A-Z]',str_3))

# match = re.search('[a-z]',str_1)
# if match:
#     print('Find letters in the str')
# else:
#     print('not found letter in the str')
    
# match = re.search('[a-zA-Z]',str_3)
# if match:
#     print('Find letters in the str')
# else:
#     print('not found letter in the str')

# print('\t',str_1,'------->', re.search('[0-9]{10}',str_1))
# print('\t',str_2,'------->', re.search('[a-z]{5}',str_2))
# print('\t',str_3,'------->', re.search('[a-zA-Z]{5}',str_3))

# match = re.search('[0-9]{10}',str_1)
# if match:
#     print('Phone normal')
# else:
#     print('Error')
# print("-------------------------------------------------")
# print('\t',str_1,'------->', re.search('[0-9]+',str_1))
# print('\t',str_1,'------->', re.search('[0-9]+',str_1).group(0))
# print('\t',str_2,'------->', re.search('[a-z]+',str_2))
# print('\t',str_3,'------->', re.search('[a-zA-Z]+',str_3))

# print('\t',str_1,'------->', re.search('[0-9]*',str_1))
# print('\t',str_2,'------->', re.search('[a-z]*',str_2))
# print('\t',str_3,'------->', re.search('[a-zA-Z]*',str_3))


# print('\t',str_3,'------->', re.search('[a-zA-Z]{3}\w',str_3))
# print('\t',str_3,'------->', re.search('^\w+',str_3))
# print('\t',str_3,'------->', re.search('^Lorem',str_3).group(0))
# print('\t',str_3,'------->', re.findall('\w+', str_3))
# print('\t',str_3,'------->', re.findall('\w+', str_3)[0])
# print('\t',str_3,'------->', re.findall('\w+', str_3)[2])

# match = re.findall('\w+', str_3)
# for item in match:
#     print(item)

# print('\t',str_3,'------->', re.sub('\w+','yellow',str_3))
# print('\t',str_3,'------->', re.sub('\w{3}','yellow',str_3))

line = "hello 3.14 bye 5,55 7.14 Olena"
match = re.findall('\d+\,\d+|\d+\.\d+', line)
print(match)
for item in match:
    print(item)
    
phone = '+38(097)123-25-36'
match = re.search('^\+38\(\d{3}\)\d{3}\-\d{2}\-\d{2}$',phone)
if match:
    print('Phone normal')
else:
    print('Error')