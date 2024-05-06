def sum_of_even_numbers(list):
    """
    This Python function calculates the sum of even numbers in a given list.
    """
    sum = 0
    for number in list:
        if number % 2 == 0:
            sum += number
    return sum
