# how to identify a string
var_1 = "sample"
print(type(var_1))

# string is mutable or not?  immutable

try:
  var_1[0]= 'T'
except Exception as error:
    print('error from mutable or not? ' + str(error))

# iterable or not? iterable

for i in var_1:
    print(i)

# ordered or not? ordered

for i in var_1:
    print(i)

 # concatanate two strings

result =  'senthil'  'kumar'
print(result)

# multiply with *

result = 'kumar ' * 5
print(result)

# Upper, lower, capital method

print('senthil'.upper())
print('SENTHIL'.lower())
print('senthil'.capitalize())

# strip white space
print('    senthil')
print('    senthil'.strip())

# split

print('senthil'.split('t'))

# upper
print ('preetha'.upper())

# lower
print('PREETHA'.lower())


var_1='sample'
print (type(var_1))


var_2 = 1
var_3 = 'preetha'
print(type(var_2))
print(type(var_3))

#concatanate two name
result  = 'preetha'  'kalimuthu'
print(result)

# multiply two name
result = 'praveen klaimuthu'* 9
print (result)

# iterable or non iterable?
for i in var_1 :
    print(i)