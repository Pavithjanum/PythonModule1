# 4
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose if the entered string is: Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS:4

# Hint: Use built-in functions of string.

in_string = input('Enter a string: ')
print('The Length of input string is ',len(in_string))

number_count = 0
char_count =0

for char in in_string:
    if char.isdigit():
        number_count = number_count+1
    else:
        char_count = char_count +1

print('LETTERS: ',char_count)
print('DIGITS: ',number_count)