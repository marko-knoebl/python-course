def fizzbuzz(max):

    for i in range(1, max):
        if i % 3 == 0 and i % 5 == 0:
            print 'fizzbuzz'
        elif i % 3 == 0:
            print 'fizz'
        elif i % 5 == 0:
            print 'buzz'
        else:
            print i

max_n = int(raw_input('Select a number'))
fizzbuzz(max_n)
