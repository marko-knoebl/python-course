import random

while True:
    print 'Neues Spiel!'

    secret_number = random.randint(1, 10)

    number = int(raw_input('bitte rate!'))

    # wiederhole solange die Zahl nicht erraten wurde
    while secret_number != number:
        print 'falsch!'
        if secret_number > number:
            print 'die gesuchte Zahl ist groesser'
        else:
            print 'die gesuchte Zahl ist kleiner'
        number = int(raw_input('bitte rate!'))


    # wenn die while-schleife beendet wurde, bedeutet das,
    # dass der benutzer richtig geraten hat.
    print 'richtig!'
