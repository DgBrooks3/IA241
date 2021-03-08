# Lab 7 While loop 

# 3.1
i = 0
while i <= 5:
    if i != 3:
        print(i)
    i = i + 1

# 3.2
i = 1
product = 1
while i <= 5:
    product = product * i
    i = i + 1
print(product)

# 3.3
i = 1
totsum = 0
while i <= 5:
    totsum = totsum + i
    i = i + 1
print(totsum)

# 3.4
i = 3
product = 1
while i <= 8:
    product = product * i
    i = i + 1
print(product)

# 3.5
i = 4
product = 1
while i <= 8:
    product = product * i
    i = i + 1
print(product)

# 3.6
num_list= [12, 32, 43, 35]
while num_list:
    num_list.remove(num_list[0])
print(num_list)