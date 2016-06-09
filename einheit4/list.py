list1 = ['hallo', 3, 3.14, True, [1, 2, 3]]

# laenge der liste
print len(list1)
print len('hallo')

# ist 3 in der Liste?
print 3 in list1

# das 2. Element der Liste
print list1[1]
# das letzte Element der Liste
print list1[-1]

# Elemente hinzufuegen
list1.append('bye')
print list1


# for-loop mit listen
# geht jeden listeneintrag durch
for element in list1:
    #print element
    print 2 * element

# for-loop mit zahlen:
# for-loop von 0 bis 9
for i in range(10):
    print i

# for-loop von 1 bis 9
for i in range(1, 10):
    print i
