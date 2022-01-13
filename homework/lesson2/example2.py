# линейный
# разветвление
# цикл


# branching
condition = True

if condition:
    print('condition is True')
else:
    print('conditipn is False')


a = 10
b = 20
variable = a > b

if variable:
    print('condition is True')
print('conditipn is False')

variable = 0
variable = None # for bool always false
if variable: #bool(variable)
    print('True')
else:
    print('False')

# логический оператор - инвертирование
a = 10
b = 110

# логическое и/или
if a > b and a > 0:  # True and True -> True
    print('True')
else:
    print('False')

# OR
if a > b or a > 0:  # True OR True -> True
    print('True')
else:
    print('False')

# and + or
if a > b or (a > b and a > 0):  # first and then or
    print('True')
else:
    print('False')



condition = 1 > 10

if condition is True:  # None
    print('True')
else:
    print('False')


variable = 10

if variable > 0:
    print('var > 0')
elif variable ==0:
    print('var == 0')
elif variable ==10:
    print('var == 10')
else:
    print('var < 0')  # can be used only with elif, no else

if variable > 0:
    print('var > 0')
    if variable > 0:
        print('var > 0')
else:
    print('var == 0')



variable1 = 10
variable2 = 20

if variable2 != 0:
    print(variable1 / variable2)
else:
    print('variable2 is 0')



if variable2 == 0:
    print('variable2 is 0')
else:
    print(variable1 / variable2)


# циклы loop while

condition = True
counter = 0
while condition:
    counter += 1
    if counter > 10:
        condition = False
    print('condition = True', counter)
print('The end')



counter = 0

while True:
    counter += 1
    if counter > 10:
        break
    print('condition = True', counter)

# counter1 = 0
# while True:
#    counter1 += 1
 #   counter2 = 0
  #
   # while TRue:
    #  counter2 += 1
     #  if cpunter2 > 10:
      #      break
       # print('inner', counter2)

counter1 = 0

while True:
    counter1 += 1
    if counter1 > 10:
        break
    if counter1 % 3 == 0:
        continue
    print('Loop', counter1)

print('The end')


my_string = 'hello '
name = 'Lilit'
print('Hello ' + name + 'HOW ARE YOU?')

tpl = 'hello {1}, how are you {0}?'  # args order during passing numbers ordering
res = tpl.format(name, 1234)
print(res)

tpl = 'hello {username}, how are you {number}?'  # args order during passing, naming of properties
res = tpl.format(username=name, number=1234)
print(res)

name = 'Lilit'
number = 123
tpl = f'hello {name}, how are you {number}?'  # add f before string and variables will be passed automatically
print(res)

my_str = 'sometest'
print(my_str.count('a'))  # count of a in string

my_str = 'some1234'
print(my_str.isalpha())  # check if all symbols are letters, True/False

my_str = '12345'
print(my_str.isdigit())  # check if all symbols are numbers, True/False

my_str = '12345'
print(my_str.isnumeric())  # ???

my_str = '12ghjk345'
print(my_str.isalnum())  # ??


my_str = 'Lilit nice girl'
print(my_str.startswith())  # check if string starts with 'L'

my_str = 'Lilit nice girl'
print(my_str.lower())  # to lowercase

my_str = 'Lilit nice girl'
print(my_str.upper())  # to uppercase

my_str = 'lilit nice girl'
print(my_str.capitalize())  # capitilise first symbol


my_str = 'lilit nice girl'
print(my_str.replace('l', 'L'))  # first symbl what to cut, 2d symbol with what replace

my_str = 'lilit nice girl'
print(my_str.find('Ad'))  # counting is starting from 0,1,2

my_str = 'lilit nice girl'
print(my_str.find('Ad', 3))  # starts finding from symbol 3

my_str = 'lilit nice girl'
print(my_str.find('Ad', 3, 5))  # starts finding from symbol 3 till 5

# slices (индексы)

my_str = 'hsvdcjhsvcHCDH'
print(my_str[0].isalpha())
print(my_str[1].isascii())
print(my_str[-1])  # last element
print(len(my_str))  # count of elements in string

my_str1 = 'A'
my_str2 = 'B'

print(my_str1 == my_str2)

my_str = input('Enter here: ')
print('Thank you')
print(my_str)
print(type(my_str))






