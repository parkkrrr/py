#!/bin/python3

lucky_numbers = [4, 8, 15, 16, 8, 8, 25, 8, 42]
friends = ["Anant", "Prakhar", "Nitin", "Aman", "Shushi"]

print(friends[1])
friends[1] = "Parker"

print(friends[1])

friends.sort()			# Sort in Asc. 
friends.extend(lucky_numbers)	# Extend 
friends.append("Pappu Bhai")	# Append 
friends.insert(1, "Aadhya")	# Insert 
friends.remove("Pappu Bhai")	# Remove
friends.pop()			# Removes the last element inside the list
print(friends.index("Parker"))	# Index
print(friends.count(8))		# Count

print(friends)

#friends.clear()		# Empty the List

friends2 = friends.copy()	# Copy
print(friends2)

lucky_numbers.reverse()		# Reverse the order
print(lucky_numbers)

#

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])

# Nested for loop

for row in number_grid:
    print(row)
