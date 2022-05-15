# Inputting three sides of the triangle
a = int(input('Enter First side(in integers): '))
b = int(input('Enter Second side(in integers): '))
c = int(input('Enter Third side(in integers): '))

# Using Logical Operators as a Conditional Statement:
Condition = (a+b>c) and (b+c>a) and (a+c>b)
Condition and print('Yes(Triangle Possible)')
Condition or print('No(Triangle not Possible)')
