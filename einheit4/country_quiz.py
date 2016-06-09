# guess the capital of a country

capitals = {
    'Austria': 'Vienna',
    'Italy': 'Rome',
    'France': 'Paris'
}

num_correct = 0

for country in capitals:
    user_answer = raw_input("What's the capital of " + country + '?\n')
    correct_answer = capitals[country]
    if user_answer == correct_answer:
        print 'correct!'
        num_correct += 1
    else:
        print 'wrong!'

percentage = float(num_correct) / len(capitals) * 100

# bonusaufgabe:
# Das Programm soll auf 2 Kommastellen runden.
# Sieh dir den string-befehl .format() an!
print 'You got ' + str(percentage) + ' right.'
