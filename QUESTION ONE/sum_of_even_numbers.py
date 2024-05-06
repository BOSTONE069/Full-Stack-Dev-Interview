def sum_of_even_numbers(list):
    sum = 0
    for number in list:
        if number % 2 == 0:  # Check if the number is even
            sum += number
    return sum
