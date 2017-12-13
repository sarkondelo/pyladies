print('This program will work as an easy calculator.')
n = int(input('Input number, please: '))
o = int(input('Input second number, please: '))
p = input('You can choose from +, -, *, and /. Please input operation: ')

if p == '+':
    print(n+o)
elif p == '-':
    print(n-o)
elif p == '*':
    print(n*o)
elif p == '/':
    print(n/o)
else:
    print('I cant understand you. Try it again, please.')
