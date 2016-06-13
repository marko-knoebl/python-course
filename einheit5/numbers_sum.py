def numbers_sum(num1, num2):
    result = num1 + num2
    return result

# test the function
assert numbers_sum(2, 4) == 6
assert numbers_sum(1, 0) == 1


def sum_list(number_list):
    # initialize the sum value
    sum = 0
    # add each number in the list
    for number in number_list:
        sum += number
    return sum

# test
assert sum_list([2, 3, 6]) == 11
assert sum_list([1, 2, 3, 4, 5, 6]) == 21

def calculator(num1, num2, operation):
    if operation == '*':
        return num1 * num2
    if operation == '-':
        return num1 - num2
    if operation == '^':
        result = 1
        for i in range(num2):
            result *= num1
        return result


assert calculator(2, 3, '*') == 6
assert calculator(1, 5, '-') == -4
assert calculator(2, 3, '^') == 8
