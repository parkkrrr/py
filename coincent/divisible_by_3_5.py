def print_divisible_3_5(num_list):
    for num in num_list:
        if num % 3 == 0 and num % 5 == 0:
            print(num)

# example usage
print_divisible_3_5([15, 30, 45, 60, 75])
