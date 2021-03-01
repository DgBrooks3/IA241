# Lab 6 For Loops and Range Function

# 3.1
for i in range(6):
    if i != 3:
        print(i)

# 3.2
product = 1
for i in range( 1, 6 ):
    product = product * i
print(product)

# 3.3
totsum = 0
for i in range( 1, 6 ):
    totsum = totsum + i
print(totsum)

# 3.4
num = 1
for i in range( 3, 9 ):
    num = num * i
print(num)

# 3.5
# 3x2x1 on top cancels with 3x2x1 on bottom, simplifies calculation to only 8x7x6x5x4
result = 1
for i in range( 4, 9 ):
    result = result * i
print(result)

# 3.6
count = 0
for i in range( len( 'this is my 6th string'.split() ) ):
    count = count + 1
print(count)

# 3.7
my_tweet = { "favorite_count":1138,"lang": "en","coordinates": (-75, 40),"entities": { "hashtags":[ "Preds", "Pens", "SingIntoSpring" ] } }
count = 0
for i in my_tweet['entities']['hashtags']:
    count = count + 1
print(count)