import random

result = random.randint(1, 45)

# returns a list of random numbers from 1 to 45 (without duplicates)
def lottery(num_draw, num_total):
    results = []
    
    # create a list of numbers 1-45
    numbers = range(1, num_total+1)
    for i in range(num_draw):
        # choose a random item from the list
        number = random.choice(numbers)
        # remove number from "numbers" list
        numbers.remove(number)

        results.append(number)
    return results

print lottery(6, 45)
print lottery(5, 10)
