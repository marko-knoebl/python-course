# helper function: ask yes/no question
#   return a boolean value (True / False)
def ask_yes_or_no(question):
    answer = raw_input(question)
    if answer == 'y' or answer == 'Y' or answer == 'yes':
        return True
    elif answer == 'n' or answer == 'N' or answer == 'no':
        return False

print "Hello! This is my online-shop!"

shopping_list = []

answer = ask_yes_or_no('Willst du einkaufen?')

while answer == True:
    new_item = raw_input("Was willst du denn einkaufen?: ")
    shopping_list.append (new_item)
    answer = ask_yes_or_no("Willst du weiter einkaufen? Y/N \n")

print "Du hast folgende Produkte gekauft:"
print shopping_list

