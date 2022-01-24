my_str = '123456789'

print(my_str[0])
print(type(my_str[0]))
print(my_str[-1])
print(my_str[1])

# slice срез строки по количеству элементов в строке
print('my_str[2:5]', my_str[2:5])
print('my_str[1:5]', my_str[1:5])
print('my_str[2:]', my_str[2:])
print('my_str[:5]', my_str[:5])
print('my_str[-2:-5]', my_str[-2:-5])
print('my_str[-2:-5]', my_str[2:9:2])
print('my_str[-2:-5]', my_str[2:9:2])
print('my_str[-2:-8:-2]', my_str[-2:-8:-2])
print('my_str[:]', my_str[:])  # string copy
print('my_str[len(my_str)//2:]', my_str[len(my_str)//2:])  # from the middle of string till the end


# list
my_str= 'abc,123,abc,ABC,new,1g1,abc,abc'
my_list = my_str.split(',')
print(my_list)
print(type(my_list))

my_list = []
print(my_list)

my_list = [1, 2.3, True, 'new', None, [1, 2, 3], ]
print(my_list)
print(my_list[0])
print(type(my_list[0]))
print(type(my_list[3].isalpha()))
print(my_list[0] + my_list[1])
print(my_list[-1][-1])

my_list[0]= '1234567'
print(my_list)

my_list[-1] [-1] = True
print(my_list)

my_list.append(123)  # add to the end of list the value
print(my_list)

my_list1 = [1, 2, 3]
my_list2 = ['1', '2', '3']
my_list3 = my_list1 + my_list2
print(my_list3)
print(my_list3 * 3)

my_list1.extend(my_list2)
print(my_list1)

my_list1.pop(0)  # removing 1st value of list
print(my_list1)

my_list1.pop(-1)  # removing the last value in a list
print(my_list1)

print(my_list1.remove('1'))  # removing the 1st exact value from the list
print(my_list1)

print(len(my_list1))
print('a' in my_list1)  # if list contains value 'a'

my_list1 = ['1', '3', '1', '4', '1', '1', '5', '9']  # removing only the first exact value
print(my_list1.remove('1'))

idx = 0
while True:
    print(my_list1[idx])
    idx += 1
    if len(my_list1) -1 < idx:
        break

my_list1 = ['1', 3, True, ['4', '1', '1', '5'], 2.3]

for element in my_list1:
    print(element)
    print(type(element))

my_list1 = ['1', 3, True, ['4', '1', '1', '5'], 2.3]
idx = 0
for element in my_list1:
    if element is '1':
        my_list1[idx] = None
        idx +=1
    print(my_list1)

my_list1 = [1, 2, 4, 100, 2, 55, 99, 4]
my_list1.sort()  # sorting values in a list
print(my_list1)

print(ord('a'))
print(ord('A'))

print('0' < '1')
print(chr(2))

my_list1.sort(reverse=True)  # sorting vice-versa
print(my_list1)

my_tuple = (1, 2, 3, [1, 2, 3, 4] 4)
my_tuple[3].append(2)
print(my_tuple)

print(bool(my_list1))
print(bool([]))

my_list4 = list('1, 2, 3, 4')
