def sum_even_numbers(num_list):
    sum = 0
    for num in num_list:
        if num % 2 == 0:
            sum += num
    return sum

# example usage
print(sum_even_numbers([1, 2, 3, 4, 5, 6]))
