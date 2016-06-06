def calculator_program():
    print 'welcome'

    valid_operations = ['addition', 'subtraction', 'a', 's', '+', '-']

    operation = raw_input('choose an operation: ')

    if operation not in valid_operations:
        print 'Invalid operation! choose + or -'
        # verlasse die Funktion
        return None

    number1 = int(raw_input('choose first number: '))
    number2 = int(raw_input('choose second number: '))

    if operation in ['addition', 'a', '+']:
        print number1 + number2
    elif operation in ['subtraction', 's', '-']:
        print number1 - number2

calculator_program()
