num_list = input("Enter a list of numbers separated by space: ").split()
odd_list = [int(num) for num in num_list if int(num) % 2 != 0]
print("Odd numbers in the list:", odd_list)
