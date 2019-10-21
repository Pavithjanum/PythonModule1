# 3
# Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number.
# The numbers obtained should be printed in a comma separated sequence on a single line.

# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
# Divide each digit with 2 and verify is it even or not.

lower_limit = 1000
upper_limit = 3000
l=[]

for n in range(lower_limit,upper_limit+1):
    num=n
    flag=1
    while n > 0:
        r = n % 10
        if r % 2 == 0:
            n = n // 10
        else:
            flag=0
            break

    if flag==1:
        l.extend([num])

print(l)