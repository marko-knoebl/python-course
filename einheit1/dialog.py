print "Hallo!"
# \n in einem String ist ein Zeilen-
#  umbruch
name = raw_input("Wie heisst du?\n")
print "Hallo, " + name + "!"
year = 2016
birth_year = raw_input("Wann bist du geboren?")

# wandle birth_year in eine Zahl (int) um
birth_year = int(birth_year)

age = year - birth_year

print "Du bist " + str(age) + " Jahre alt"
print "Du bist {0} Jahre alt".format(age)

if age < 20:
    print "Du bist jung"
else:
    print "Du bist alt"
