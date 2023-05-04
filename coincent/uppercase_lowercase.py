input_str = input("Enter a string: ")
output_str = ""
for char in input_str:
    if char.islower():
        output_str += char.upper()
    elif char.isupper():
        output_str += char.lower()
    else:
        output_str += char
print("Output string:", output_str)
