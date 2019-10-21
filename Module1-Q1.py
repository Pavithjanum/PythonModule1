# 1
# Write a program which will find factors of given number and find whether the factor is even or odd.
# Hint: Use Loop with if-else statements

num = int(input('Enter a number greater then zero:'))
factors=[]
print(('number is %i')%(num))

for n in range(1,num+1):
    if num%n == 0:
        print(('Factorial of %i is %i')%(num,n))
        factors.extend([n])
        if n%2 == 0:
            print('Factor %i is even'%(n))
        else:
            print('Factor %i is odd' %(n))
    else:
        continue

print(factors)

even_odd=[]
for c in factors:
    if c%2 == 0:
        even_odd.extend(['Even'])
    else:
        even_odd.extend(['Odd'])

print(even_odd)

