# lecture on list and set

my_List = [1, 2, 3, 4, 5]
print(my_List)

my_nested_list = [1, 2, 3, my_List]
print(my_nested_list)

my_List[0] = 6
print(my_List)
my_List.append(7)
print(my_List)
my_List.remove(7)
print(my_List)

my_List.sort()
print(my_List)

my_List.reverse()
print(my_List)

print(my_List + [8, 9])

my_List.extend(['a', 'b'])
print(my_List)
print('c' in my_List)

print(len(my_List))

print(len('hello world'))

# print(my_List[:])

# x, y = ['a', 'b']
# print(y)