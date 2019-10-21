# 5
# Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.

input_number = input('Enter a number to check for Palindrome :')
if input_number.isdigit():
    orig_str=str(input_number)
    rev_str = input_number[::-1]
    if orig_str == rev_str:
        print('The Given number %i is Palindrome'%int(orig_str))
    else:
        print('The Given number %i is not a Palindrome'%int(orig_str))

else:
    print('Numbers are only allowed to enter')
