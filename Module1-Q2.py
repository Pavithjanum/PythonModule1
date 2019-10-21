# 2

# Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

import sys

inputs = sys.argv

print('Raw inputs from user',inputs[1:])

String_inputs = inputs[1:]

String_outputs = sorted(String_inputs)
print(String_outputs)

print('Your Strings in Sorted order:')
for string in String_outputs:
    print(string)
