def square_except_3(num_list):
    for num in num_list:
        if num % 3 == 0:
            continue
        print(num ** 2)

# example usage
square_except_3([1, 2, 3, 4, 5, 6])
