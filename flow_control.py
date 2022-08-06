number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for exponentiation
''')
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
elif operation == '**':
    print('{} ** {} = '.format(number_1, number_2))
    print(number_1 ** number_2)
if operation == "@":
    print("Incorrect sign")
if operation == "#":
     print("Incorrect sign")
if operation == ":":
    print("Incorrect sign")
if operation == "%":
    print("Incorrect sign")