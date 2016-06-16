# datentypen

# boolean
b = True

# string
name = 'Marko'
last_name = "Knoebl"

# int
a = 3
# float
pi = 3.14

# list
l = [1, 2, False, 'test']
l.append(3)
print l[2]

# dict
d = {'a': 3, 'b': 'hallo'}
print d['a']

# function
def sum(a, b):
    return a + b


# schleifen
a = 0
while a < 10:
    print a
    a = a + 1

for item in l:
    print item

for i in range(10):
    print i


# if
num = 14

if num < 10:
    print 'kleiner 10'
elif num == 10:
    print 'gleich 10'
else:
    print 'groesser 10'
